#include <cstdio>
#include <cstdint>
#include <chrono>

static inline double calculate(uint32_t iterations, int64_t p1, int64_t p2) {
    double result = 1.0;
    int64_t j = p1 - p2;                 // j_minus for i=1
    const int64_t add = 2 * p2;          // j_plus = j_minus + 2*param2
    const int64_t step = p1;             // increment for next i

    uint32_t i = 0;
    uint32_t n_unrolled = (iterations / 8) * 8;

    for (; i < n_unrolled; i += 8) {
        result -= 1.0 / (double)j; result += 1.0 / (double)(j + add); j += step;
        result -= 1.0 / (double)j; result += 1.0 / (double)(j + add); j += step;
        result -= 1.0 / (double)j; result += 1.0 / (double)(j + add); j += step;
        result -= 1.0 / (double)j; result += 1.0 / (double)(j + add); j += step;
        result -= 1.0 / (double)j; result += 1.0 / (double)(j + add); j += step;
        result -= 1.0 / (double)j; result += 1.0 / (double)(j + add); j += step;
        result -= 1.0 / (double)j; result += 1.0 / (double)(j + add); j += step;
        result -= 1.0 / (double)j; result += 1.0 / (double)(j + add); j += step;
    }
    for (; i < iterations; ++i) {
        result -= 1.0 / (double)j;
        result += 1.0 / (double)(j + add);
        j += step;
    }
    return result;
}

int main() {
    using clock = std::chrono::steady_clock;
    auto start_time = clock::now();

    double result = calculate(200000000u, 4, 1) * 4.0;

    auto end_time = clock::now();
    double elapsed = std::chrono::duration<double>(end_time - start_time).count();

    std::printf("Result: %.12f\n", result);
    std::printf("Execution Time: %.6f seconds\n", elapsed);
    return 0;
}