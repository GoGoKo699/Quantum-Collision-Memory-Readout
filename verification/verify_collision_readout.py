import numpy as np


I = np.eye(2)
X = np.array([[0, 1], [1, 0]])
Y = np.array([[0, -1j], [1j, 0]])
Z = np.diag([1, -1])
PAULI = (X, Y, Z)
SWAP = np.eye(4)[[0, 2, 1, 3]]


def operator(vector):
    return sum(value * pauli for value, pauli in zip(vector, PAULI))


def collide(theta, system, environment):
    unitary = np.cos(theta) * np.eye(4) - 1j * np.sin(theta) * SWAP
    return unitary @ np.kron(system, environment) @ unitary.conj().T


def trace_system(joint):
    return np.trace(joint.reshape(2, 2, 2, 2), axis1=0, axis2=2)


def trace_environment(joint):
    return np.trace(joint.reshape(2, 2, 2, 2), axis1=1, axis2=3)


def second(theta, env, eta, reset):
    shrunk = eta * env + (1 - eta) * np.trace(env) * I / 2
    return trace_environment(collide(theta, reset, shrunk))


def measure_chi_squared(p, q):
    return sum(float((a - b) ** 2 / b) for a, b in zip(p, q) if b > 1e-13)


def probabilities(state, observ):
    return np.array([np.trace(state @ (I + sign * observ) / 2).real for sign in (-1, 1)])


def random_povm(rng, count):
    noise = rng.normal(size=(count, 2, 2)) + 1j * rng.normal(size=(count, 2, 2))
    raw = noise @ noise.conj().transpose(0, 2, 1)
    values, vectors = np.linalg.eigh(sum(raw))
    isqrt = (vectors * values ** -0.5) @ vectors.conj().T
    return [isqrt @ effect @ isqrt for effect in raw]


rng = np.random.default_rng(690211)
up = (I + Z) / 2
down = (I - Z) / 2
for _ in range(400):
    theta1, theta2 = rng.uniform(-np.pi, np.pi, 2)
    eta = rng.uniform(0.01, 1)
    s1, s2 = np.sin([theta1, theta2])
    joint = collide(theta1, up, I / 2)
    env_after_flip = trace_system(np.kron(down, I) @ joint)
    np.testing.assert_allclose(env_after_flip, s1**2 * up / 2, atol=1e-13)

    for sign in (-1, 1):
        reset = (I + sign * Z) / 2
        opposite = (I - sign * Z) / 2
        observed = np.trace(opposite @ second(theta2, env_after_flip, eta, reset)).real
        expected = s1**2 * s2**2 * (1 - eta * sign) / 4
        np.testing.assert_allclose(observed, expected, atol=1e-13)

        signed_joint = collide(theta1, reset, I / 2)
        blind = np.trace(down @ second(theta2, trace_system(signed_joint), eta, up)).real
        np.testing.assert_allclose(blind, s2**2 * (1 - eta * s1**2 * sign) / 2, atol=1e-13)

    # Known-angle bound attainer uses an intermediate X measurement and X reset.
    x_reset = (I + X) / 2
    measured = 0
    for sign in (-1, 1):
        effect = (I + sign * X) / 2
        env = trace_system(np.kron(effect, I) @ joint)
        alternative = second(theta2, env, eta, x_reset)
        null = second(theta2, env, 0, x_reset)
        diff = alternative - null
        axis = diff / max(np.linalg.norm(diff, ord=2), 1e-20)
        measured += measure_chi_squared(probabilities(alternative, axis), probabilities(null, axis))
    np.testing.assert_allclose(measured, eta**2 * s1**2 * s2**2, atol=1e-12)

    env = trace_system(joint)
    alternative = second(theta2, env, eta, x_reset)
    null = second(theta2, env, 0, x_reset)
    diff = alternative - null
    axis = diff / max(np.linalg.norm(diff, ord=2), 1e-20)
    measured = measure_chi_squared(probabilities(alternative, axis), probabilities(null, axis))
    np.testing.assert_allclose(measured, eta**2 * s1**4 * s2**2, atol=1e-12)

    measured = 0
    for effect in random_povm(rng, int(rng.integers(1, 7))):
        env = trace_system(np.kron(effect, I) @ joint)
        vector = rng.normal(size=3)
        vector = vector / np.linalg.norm(vector) * rng.uniform(0, 1)
        reset = (I + operator(vector)) / 2
        alternative = second(theta2, env, eta, reset)
        null = second(theta2, env, 0, reset)
        final = random_povm(rng, int(rng.integers(1, 7)))
        probs = [np.trace(effect @ alternative).real for effect in final]
        null_probs = [np.trace(effect @ null).real for effect in final]
        measured += measure_chi_squared(probs, null_probs)
    assert measured <= eta**2 * s1**2 * s2**2 + 1e-12

print('400 seeded signed-angle pairs: both exact event laws, both chi-square attainers, and arbitrary-POVM checks passed.')

for _ in range(250):
    theta1, theta2 = rng.uniform(-np.pi, np.pi, 2)
    p1, p2 = np.sin([theta1, theta2]) ** 2
    trial = rng.normal(size=(8, 2)) + 1j * rng.normal(size=(8, 2))
    kraus = np.linalg.qr(trial)[0].reshape(4, 2, 2)
    first_axis, second_axis = rng.integers(0, 3, 2)
    u, v = PAULI[first_axis], PAULI[second_axis]

    def bath_channel(state):
        return sum(operator @ state @ operator.conj().T for operator in kraus)

    ell = np.trace(v @ bath_channel(I / 2)).real
    transfer = np.trace(v @ bath_channel(u / 2)).real
    q = rng.uniform(0, 0.5)
    kappa = 1 - 2 * q
    report_flip_mass = q + kappa * p1 / 2
    total = polarity_total = product_total = 0
    for initial in (-1, 1):
        system = (I + initial * u) / 2
        first_flip = (I - initial * u) / 2
        joint = collide(theta1, system, I / 2)
        heralded = trace_system(np.kron(first_flip, I) @ joint)
        for reset_sign in (-1, 1):
            reset = (I + reset_sign * v) / 2
            final_flip = (I - reset_sign * v) / 2
            output = trace_environment(collide(theta2, reset, bath_channel(heralded)))
            probability = np.trace(final_flip @ output).real
            expected = p1 * p2 * (1 - reset_sign * (ell + initial * transfer)) / 4
            np.testing.assert_allclose(probability, expected, atol=1e-13)
            for report in (0, 1):
                mass = report_flip_mass if report else 1 - report_flip_mass
                flip_weight = 1 - q if report else q
                bath_branch = (flip_weight * heralded
                               + (1 - flip_weight) * (trace_system(joint) - heralded))
                noisy_output = trace_environment(
                    collide(theta2, reset, bath_channel(bath_branch))
                )
                got = np.trace(final_flip @ noisy_output).real
                want = p2 / 2 * (mass * (1 - reset_sign * ell)
                                 - p1 / 2 * initial * reset_sign * transfer)
                np.testing.assert_allclose(got, want, atol=1e-13)
            total += probability / 4
            polarity_total += reset_sign * probability / 4
            product_total += initial * reset_sign * probability / 4
    np.testing.assert_allclose(total, p1 * p2 / 4, atol=1e-13)
    np.testing.assert_allclose(polarity_total, -ell * total, atol=1e-13)
    np.testing.assert_allclose(product_total, -transfer * total, atol=1e-13)

print('250 seeded qubit CPTP maps: full affine-channel event law and its two conditional moment identities passed.')

for _ in range(400):
    p1, p2, eta = rng.uniform(0.001, 1, 3)
    q = rng.uniform(0, 0.5)
    theta1, theta2 = np.arcsin(np.sqrt([p1, p2]))
    joint = (collide(theta1, up, I / 2) + collide(-theta1, up, I / 2)) / 2
    observed_chi_squared = 0
    for sign in (-1, 1):
        effect = (I + sign * (1 - 2*q) * Z) / 2
        bath_branch = trace_system(np.kron(effect, I) @ joint)
        alternative = (second(theta2, bath_branch, eta, up)
                       + second(-theta2, bath_branch, eta, up)) / 2
        null = second(theta2, bath_branch, 0, up)
        observed_chi_squared += measure_chi_squared(
            probabilities(alternative, Z), probabilities(null, Z)
        )
    exact = eta**2 * p1**2 * p2 / (
        (2-p2) * (1 - (1-2*q)**2 * (1-p1)**2)
    )
    np.testing.assert_allclose(observed_chi_squared, exact, atol=1e-12)

print('Noisy affine laws and 400 sign-dithered noisy divergence checks passed.')
