# What is TDD (Test-Driven Development)?

Test-Driven Development (TDD) is a software development methodology where tests are written before the actual code. It follows a cycle of **Red-Green-Refactor**:

1. **Red**: Write a test for a new feature or functionality. Run the test, and it should fail because the feature is not implemented yet.

2. **Green**: Write the minimum amount of code required to make the test pass. Focus on functionality, not optimization.

3. **Refactor**: Refactor the code to improve its structure and readability while ensuring the test still passes.

## Benefits of TDD
- Ensures code correctness.
- Encourages modular and maintainable code.
- Provides a safety net for refactoring.
- Improves developer confidence.

## Example Workflow
1. Write a test for a function that calculates the factorial of a number.
2. Run the test (it fails).
3. Implement the factorial function.
4. Run the test again (it passes).
5. Refactor the function for better readability or performance.