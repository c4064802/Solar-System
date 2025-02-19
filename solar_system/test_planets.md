# Test Plan for Solar System Program

## **1. Functional Testing**
| Test Case | Input | Expected Output |
|-----------|-------|----------------|
| Load planets | planets.txt | Dictionary with correct planet objects |
| Query planet | "Tell me about Earth" | Correct details of Earth |
| Query mass | "How massive is Mars?" | Mass of Mars displayed correctly |
| Check existence | "Is Pluto in the list?" | Correct response |
| Count moons | "How many moons does Jupiter have?" | Correct moon count |

## **2. Edge Cases**
| Test Case | Input | Expected Output |
|-----------|-------|----------------|
| Non-existent planet | "Tell me about Vulcan" | "Planet not found" message |
| Invalid input | Entering numbers instead of names | Error message |
| Case insensitivity | "earth", "Earth", "EARTH" | Should work the same |

## **3. Unit Testing**
- Test planet creation
- Test loading from file
- Test querying functionalities

## **4. Performance Testing**
- Measure response time with large data sets
