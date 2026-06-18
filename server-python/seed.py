from datetime import datetime
import bcrypt
from config.db import db

def hash_pw(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

units_data = [
    # JavaScript
    {
        "title": "JS Basics & Functions",
        "unit_number": 1,
        "content": "Introduction to JavaScript, variables (var/let/const), data types, operators, control structures (if/else/switch), loops (for/while/do-while), and functions (declaration, expression, arrow functions, scope).",
        "category": "javascript",
        "author": "Admin",
        "sections": [
            {
                "heading": "What is JavaScript?",
                "summary": "JavaScript is a high-level interpreted language used to add interactivity and dynamic behavior to web pages. It runs in browsers and on the server via Node.js, and is one of the core technologies of modern web development.",
                "body_html": """<p>JavaScript is a <strong>high-level, interpreted programming language</strong> used to add interactivity and dynamic behavior to web pages. It runs directly in web browsers and can also be used for server-side development through technologies like Node.js.</p>
<p>It is one of the core technologies of modern web development and has a vast ecosystem of tools, libraries, and frameworks.</p>
<h3>Where is JavaScript Used?</h3>
<ul>
  <li>Web applications for creating interactive user interfaces</li>
  <li>Mobile application development</li>
  <li>Server-side programming</li>
  <li>Game development and animations</li>
</ul>"""
            },
            {
                "heading": "Variables in JavaScript",
                "summary": "Variables store and manage data. Use const for fixed values and let when reassignment is needed. Avoid var as it has function-level scope and allows redeclaration, which can cause unexpected behavior.",
                "body_html": """<p>Variables store and manage data within a program. JavaScript provides three types of variable declarations:</p>
<table>
  <thead><tr><th>Keyword</th><th>Scope</th><th>Redeclare</th><th>Reassign</th></tr></thead>
  <tbody>
    <tr><td>var</td><td>Function</td><td>Yes</td><td>Yes</td></tr>
    <tr><td>let</td><td>Block</td><td>No</td><td>Yes</td></tr>
    <tr><td>const</td><td>Block</td><td>No</td><td>No</td></tr>
  </tbody>
</table>
<blockquote>Best Practice: Prefer <strong>const</strong> for fixed values and <strong>let</strong> when reassignment is required. Avoid <strong>var</strong> in modern development.</blockquote>"""
            },
            {
                "heading": "Data Types",
                "summary": "JavaScript is dynamically typed. Primitive types include Number, String, Boolean, Undefined, and Null. Non-primitive types include Arrays (collections of values) and Objects (key-value pairs).",
                "body_html": """<p>JavaScript uses <strong>dynamic typing</strong> — the type of a variable is determined at runtime.</p>
<table>
  <thead><tr><th>Category</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>Primitive</td><td>Number</td><td>Numeric values</td></tr>
    <tr><td>Primitive</td><td>String</td><td>Text data</td></tr>
    <tr><td>Primitive</td><td>Boolean</td><td>Logical values: true or false</td></tr>
    <tr><td>Primitive</td><td>Undefined</td><td>Declared but not assigned a value</td></tr>
    <tr><td>Primitive</td><td>Null</td><td>Intentional absence of value</td></tr>
    <tr><td>Non-Primitive</td><td>Array</td><td>Collection of multiple values in one variable</td></tr>
    <tr><td>Non-Primitive</td><td>Object</td><td>Key-value pairs for structured data</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Operators",
                "summary": "Arithmetic operators perform math calculations. Comparison operators compare values and return boolean results. Strict comparison checks both value and type. Logical operators combine or evaluate multiple conditions.",
                "body_html": """<table>
  <thead><tr><th>Type</th><th>Purpose</th></tr></thead>
  <tbody>
    <tr><td>Arithmetic</td><td>Perform mathematical calculations</td></tr>
    <tr><td>Comparison</td><td>Compare values and return a boolean result; strict comparison checks value and type</td></tr>
    <tr><td>Logical</td><td>Combine multiple conditions and evaluate logical expressions</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Control Structures",
                "summary": "Control structures determine execution flow. Conditional statements execute code based on conditions. Switch is used when multiple conditions depend on a single value for cleaner, more structured code.",
                "body_html": """<p>Control structures determine the flow of execution in a program.</p>
<table>
  <thead><tr><th>Structure</th><th>Purpose</th></tr></thead>
  <tbody>
    <tr><td>if / else</td><td>Executes code based on whether a condition is true or false</td></tr>
    <tr><td>else if</td><td>Handles multiple conditions in sequence</td></tr>
    <tr><td>switch</td><td>Selects one block among many when multiple conditions depend on a single value</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Loops",
                "summary": "Loops execute code repeatedly. For loops are used when iterations are known. While loops run while a condition is true. Do-while loops execute at least once before checking the condition.",
                "body_html": """<table>
  <thead><tr><th>Loop</th><th>When to Use</th></tr></thead>
  <tbody>
    <tr><td>for</td><td>When the number of iterations is known</td></tr>
    <tr><td>while</td><td>Executes as long as a condition remains true</td></tr>
    <tr><td>do-while</td><td>Executes the code at least once before checking the condition</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Functions",
                "summary": "Functions are reusable code blocks that accept parameters and return outputs. JavaScript supports standard functions, expressions, arrow functions, default parameters, and callback functions.",
                "body_html": """<p>Functions are reusable blocks of code designed to perform specific tasks. They improve code reusability and organization.</p>
<table>
  <thead><tr><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>Standard Function</td><td>Declared with the function keyword</td></tr>
    <tr><td>Function Expression</td><td>Assigned to a variable</td></tr>
    <tr><td>Arrow Function</td><td>Modern and concise syntax</td></tr>
    <tr><td>Default Parameters</td><td>Fallback values when no argument is provided</td></tr>
    <tr><td>Callback Function</td><td>A function passed as an argument to another function</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Scope",
                "summary": "Scope defines where variables can be accessed. Global scope is everywhere, function scope is inside a function, and block scope is inside curly braces using let or const. Understanding scope prevents conflicts.",
                "body_html": """<p>Scope defines where variables can be accessed within a program.</p>
<table>
  <thead><tr><th>Scope Type</th><th>Accessible</th></tr></thead>
  <tbody>
    <tr><td>Global Scope</td><td>Variables accessible throughout the program</td></tr>
    <tr><td>Function Scope</td><td>Variables accessible only within a function</td></tr>
    <tr><td>Block Scope</td><td>Variables accessible only within a specific block of code</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Hoisting",
                "summary": "Hoisting moves variable and function declarations to the top of their scope before execution. Different declaration types behave differently during hoisting, which can cause unexpected results if misunderstood.",
                "body_html": """<p>Hoisting is a behavior in JavaScript where variable and function declarations are moved to the top of their scope before execution.</p>
<ul>
  <li>Different types of variable declarations behave differently during hoisting</li>
  <li>Improper understanding of hoisting can lead to unexpected results</li>
  <li>Modern declarations are safer and more predictable than older ones</li>
</ul>"""
            },
            {
                "heading": "Best Practices and Conclusion",
                "summary": "Avoid var, confusing comparisons, and global variables. Use const and let, write small reusable functions, and follow consistent standards. These fundamentals are the foundation for advanced JavaScript and web development.",
                "body_html": """<h3>Common Mistakes</h3>
<ul>
  <li>Using outdated variable declarations</li>
  <li>Confusing different types of comparison operations</li>
  <li>Forgetting to return values from functions</li>
  <li>Misunderstanding variable scope</li>
</ul>
<h3>Best Practices</h3>
<ul>
  <li>Use modern variable declarations for better control</li>
  <li>Write clean, readable, and maintainable code</li>
  <li>Break logic into small, reusable functions</li>
  <li>Avoid unnecessary global variables</li>
  <li>Follow consistent coding standards</li>
</ul>
<p>A strong understanding of these concepts is essential for building interactive applications and progressing to advanced topics such as frameworks, asynchronous programming, and backend development.</p>"""
            },
        ],
        "quiz": [
            {"question": "Which keyword declares a block-scoped variable in JS?", "options": ["var", "let", "function", "static"], "answer": 1},
            {"question": "What does an arrow function use instead of the 'function' keyword?", "options": ["=>", "->", "::", ">>"], "answer": 0},
            {"question": "Which loop always executes its body at least once?", "options": ["for", "while", "do-while", "foreach"], "answer": 2},
            {"question": "Which scope type makes a variable accessible only inside a function?", "options": ["Block scope", "Global scope", "Function scope", "Module scope"], "answer": 2},
            {"question": "What is hoisting in JavaScript?", "options": ["Moving code to a new file", "Declarations moved to top of scope before execution", "Copying variables", "Deleting unused variables"], "answer": 1},
        ]
    },
    # JavaScript Unit 2
    {
        "title": "ES6 Features",
        "unit_number": 2,
        "content": "ES6 (ECMAScript 2015) features: let and const, template literals, destructuring, spread operator, rest operator, and modules (import/export).",
        "category": "javascript",
        "author": "Admin",
        "sections": [
            {
                "heading": "Introduction to ES6",
                "summary": "ES6 (ECMAScript 2015) is a major update to JavaScript that introduced modern features to make the language more powerful, readable, and easier to use. It forms the foundation for frameworks like React and modern backend development.",
                "body_html": """<p>ES6 (ECMAScript 2015) is a <strong>major update to JavaScript</strong> that introduced modern features to make the language more powerful, readable, and easier to use. It provides improved syntax and new capabilities that are widely used in modern web development.</p>
<p>ES6 helps developers write cleaner and more maintainable code, and it forms the foundation for frameworks like React and modern backend development.</p>"""
            },
            {
                "heading": "Let and Const",
                "summary": "ES6 introduced let and const to replace var. let is block-scoped and allows reassignment. const is block-scoped and cannot be reassigned. Use const by default and let only when reassignment is required.",
                "body_html": """<p>ES6 introduced two new ways to declare variables: <strong>let</strong> and <strong>const</strong>, replacing many issues associated with older variable declarations.</p>
<table>
  <thead><tr><th>Keyword</th><th>Scope</th><th>Reassignable</th><th>Use When</th></tr></thead>
  <tbody>
    <tr><td>let</td><td>Block</td><td>Yes</td><td>Value changes over time</td></tr>
    <tr><td>const</td><td>Block</td><td>No</td><td>Value should remain constant</td></tr>
  </tbody>
</table>
<blockquote>Best Practice: Use <strong>const</strong> by default and <strong>let</strong> only when reassignment is required.</blockquote>"""
            },
            {
                "heading": "Template Literals",
                "summary": "Template literals provide a flexible way to work with strings. They allow embedding variables and expressions directly within strings and support multi-line strings without special formatting.",
                "body_html": """<p>Template literals provide a more flexible and readable way to work with strings.</p>
<ul>
  <li>Allow embedding variables and expressions directly within strings</li>
  <li>Make it easier to construct dynamic content</li>
  <li>Support multi-line strings without requiring special formatting</li>
</ul>
<p>Template literals improve code readability and reduce complexity when working with text.</p>"""
            },
            {
                "heading": "Destructuring",
                "summary": "Destructuring allows extracting values from arrays or properties from objects into separate variables. It simplifies working with complex data structures and makes code shorter and easier to understand.",
                "body_html": """<p>Destructuring is a feature that allows extracting values from arrays or properties from objects into separate variables.</p>
<ul>
  <li>Simplifies working with complex data structures</li>
  <li>Reduces the need for repetitive access operations</li>
  <li>Makes code shorter, cleaner, and easier to understand</li>
</ul>
<p>Destructuring is commonly used in modern JavaScript, especially in frameworks where handling structured data is frequent.</p>"""
            },
            {
                "heading": "Spread Operator",
                "summary": "The spread operator expands elements of an array or properties of an object into individual elements. It is useful for copying data, combining arrays or objects, and passing values flexibly.",
                "body_html": """<p>The spread operator is used to expand elements of an array or properties of an object into individual elements.</p>
<ul>
  <li>Useful for copying data</li>
  <li>Combining multiple arrays or objects</li>
  <li>Passing values in a flexible way</li>
</ul>
<p>The spread operator improves code efficiency and reduces the need for manual copying or merging.</p>"""
            },
            {
                "heading": "Rest Operator",
                "summary": "The rest operator collects multiple values into a single structure, typically an array. It is used in functions to handle a variable number of arguments, making functions more flexible.",
                "body_html": """<p>The rest operator is used to collect multiple values into a single structure, typically as an array.</p>
<ul>
  <li>Commonly used in functions to handle a variable number of arguments</li>
  <li>Makes functions more flexible and adaptable to different inputs</li>
  <li>Helps in managing dynamic data efficiently</li>
</ul>"""
            },
            {
                "heading": "Modules (Import and Export)",
                "summary": "Modules allow splitting code into separate files and organizing it into reusable parts. Exporting makes elements available outside a file. Importing accesses those elements in another file.",
                "body_html": """<p>Modules allow splitting code into separate files and organizing it into smaller, reusable parts.</p>
<table>
  <thead><tr><th>Operation</th><th>Purpose</th></tr></thead>
  <tbody>
    <tr><td>Export</td><td>Makes variables, functions, or classes available outside a file</td></tr>
    <tr><td>Import</td><td>Accesses exported elements in another file</td></tr>
  </tbody>
</table>
<p>Modules improve code organization, maintainability, and scalability, especially in large applications. They are essential in modern development, enabling structured and modular programming.</p>"""
            },
            {
                "heading": "Conclusion",
                "summary": "ES6 features make JavaScript more readable, structured, and efficient. Understanding these concepts is essential for modern web development and prepares developers for advanced topics and frameworks.",
                "body_html": """<p>ES6 features enhance JavaScript by making it:</p>
<ul>
  <li>More readable</li>
  <li>More structured</li>
  <li>More efficient</li>
</ul>
<p>Understanding these concepts is essential for modern web development, as they are widely used in frameworks, libraries, and real-world applications. Mastering ES6 prepares developers for advanced topics and helps in writing clean, maintainable code.</p>"""
            },
        ],
        "quiz": [
            {"question": "Which ES6 keyword declares a block-scoped variable that cannot be reassigned?", "options": ["var", "let", "const", "static"], "answer": 2},
            {"question": "What do template literals use to embed expressions inside strings?", "options": ["Single quotes", "Double quotes", "Backticks", "Brackets"], "answer": 2},
            {"question": "What does destructuring allow you to do?", "options": ["Delete variables", "Extract values from arrays or objects into variables", "Copy functions", "Merge files"], "answer": 1},
            {"question": "What does the spread operator do?", "options": ["Collects values into an array", "Deletes array elements", "Expands elements of an array or object", "Imports modules"], "answer": 2},
            {"question": "Which ES6 feature allows splitting code into separate reusable files?", "options": ["Destructuring", "Template Literals", "Modules", "Rest Operator"], "answer": 2},
        ]
    },
    # JavaScript Unit 3
    {
        "title": "Asynchronous JavaScript",
        "unit_number": 3,
        "content": "Asynchronous JavaScript: callbacks, promises, async/await, Fetch API, and error handling in asynchronous operations.",
        "category": "javascript",
        "author": "Admin",
        "sections": [
            {
                "heading": "Introduction to Asynchronous JavaScript",
                "summary": "Asynchronous JavaScript allows a program to execute tasks without blocking other operations. It improves performance and responsiveness, especially in web applications handling multiple tasks simultaneously.",
                "body_html": """<p>Asynchronous JavaScript allows a program to execute tasks <strong>without blocking</strong> the execution of other operations. This means that long-running tasks, such as fetching data from a server, do not stop the rest of the program from running.</p>
<p>It improves performance and responsiveness, especially in web applications where multiple tasks need to be handled simultaneously.</p>"""
            },
            {
                "heading": "Callbacks",
                "summary": "Callbacks are functions passed as arguments to another function and executed after a task completes. They handle asynchronous tasks and ensure proper execution order but can lead to complex nested structures.",
                "body_html": """<p>Callbacks are one of the earliest ways to handle asynchronous operations in JavaScript.</p>
<p>A callback is a function that is passed as an argument to another function and is executed after a specific task is completed.</p>
<ul>
  <li>Used to handle asynchronous tasks</li>
  <li>Ensures proper execution order</li>
  <li>Can lead to complex nested structures when overused</li>
</ul>
<p>This complexity is often referred to as <strong>callback nesting</strong>, which makes code harder to read and maintain.</p>"""
            },
            {
                "heading": "Promises",
                "summary": "Promises represent a value that may be available now, later, or never. They have states: pending, fulfilled, and rejected. Promises provide a cleaner way to handle async tasks and avoid deeply nested code.",
                "body_html": """<p>Promises were introduced to improve the handling of asynchronous operations and overcome the limitations of callbacks.</p>
<table>
  <thead><tr><th>State</th><th>Meaning</th></tr></thead>
  <tbody>
    <tr><td>Pending</td><td>Operation is still in progress</td></tr>
    <tr><td>Fulfilled</td><td>Operation completed successfully</td></tr>
    <tr><td>Rejected</td><td>Operation failed</td></tr>
  </tbody>
</table>
<ul>
  <li>Allows handling success and failure separately</li>
  <li>Improves readability and avoids deeply nested code</li>
</ul>"""
            },
            {
                "heading": "Async/Await",
                "summary": "Async/Await is a modern approach built on promises that simplifies asynchronous programming. It allows writing async code that looks like synchronous code, making it easier to read and maintain.",
                "body_html": """<p>Async/Await is a modern approach built on top of promises that simplifies asynchronous programming.</p>
<p>It allows developers to write asynchronous code in a style that looks similar to synchronous code, making it easier to read and maintain.</p>
<ul>
  <li>Simplifies promise handling</li>
  <li>Improves code readability</li>
  <li>Makes error handling more straightforward</li>
</ul>
<p>Async/Await is widely used in modern JavaScript applications due to its simplicity.</p>"""
            },
            {
                "heading": "Fetch API",
                "summary": "The Fetch API is used to make network requests such as retrieving data from servers. It supports asynchronous operations and is commonly used for working with web APIs to enable dynamic content updates.",
                "body_html": """<p>The Fetch API is used to make network requests, such as retrieving data from servers.</p>
<ul>
  <li>Used for sending and receiving data over the network</li>
  <li>Supports asynchronous operations</li>
  <li>Commonly used for working with web APIs</li>
</ul>
<p>Fetch plays a crucial role in building data-driven applications.</p>"""
            },
            {
                "heading": "Error Handling in Asynchronous JavaScript",
                "summary": "Error handling ensures programs manage failures gracefully. In async programming, errors can occur during network requests or data processing and must be caught to maintain application stability.",
                "body_html": """<p>Error handling ensures that programs can manage failures gracefully without crashing.</p>
<ul>
  <li>Errors should be properly caught and handled</li>
  <li>Helps maintain application stability</li>
  <li>Provides meaningful feedback to users</li>
</ul>
<p>Proper error handling is essential for building reliable and robust applications.</p>"""
            },
            {
                "heading": "Advantages and Challenges",
                "summary": "Async programming improves performance and allows handling multiple tasks simultaneously. However, it can be difficult for beginners and requires careful error management to avoid unexpected behavior.",
                "body_html": """<h3>Advantages</h3>
<ul>
  <li>Improves application performance</li>
  <li>Allows handling multiple tasks simultaneously</li>
  <li>Enhances user experience by preventing blocking operations</li>
  <li>Essential for modern web applications</li>
</ul>
<h3>Challenges</h3>
<ul>
  <li>Can be difficult to understand for beginners</li>
  <li>Improper handling can lead to unexpected behavior</li>
  <li>Requires careful error management</li>
</ul>"""
            },
            {
                "heading": "Conclusion",
                "summary": "Asynchronous JavaScript is fundamental for modern web development. Understanding callbacks, promises, async/await, and Fetch enables building responsive applications that work with APIs and handle real-time data.",
                "body_html": """<p>Asynchronous JavaScript is a fundamental concept for modern web development. Understanding callbacks, promises, async/await, and data fetching is essential for building responsive and efficient applications.</p>
<p>Mastering these concepts enables developers to work with APIs, handle real-time data, and create smooth user experiences.</p>"""
            },
        ],
        "quiz": [
            {"question": "What is a callback in JavaScript?", "options": ["A variable that stores data", "A function passed as an argument executed after a task", "A loop that runs asynchronously", "A type of promise"], "answer": 1},
            {"question": "Which promise state means the operation completed successfully?", "options": ["Pending", "Rejected", "Fulfilled", "Resolved"], "answer": 2},
            {"question": "What is Async/Await built on top of?", "options": ["Callbacks", "Fetch API", "Promises", "Event Listeners"], "answer": 2},
            {"question": "Which API is used to make network requests in JavaScript?", "options": ["DOM API", "Fetch API", "Storage API", "Canvas API"], "answer": 1},
            {"question": "What is the main advantage of asynchronous programming?", "options": ["Runs code faster by skipping errors", "Allows multiple tasks without blocking execution", "Removes the need for functions", "Simplifies variable declarations"], "answer": 1},
        ]
    },
    # Python
    {
        "title": "Python Fundamentals",
        "unit_number": 1,
        "content": "Introduction to Python, variables and data types, input/output, operators, conditional statements (if/elif/else), loops (for/while), and data structures: lists, tuples, sets, dictionaries.",
        "category": "python",
        "author": "Admin",
        "sections": [
            {
                "heading": "Introduction to Python",
                "summary": "Python is a high-level interpreted language known for simplicity and readability. It is open-source, platform-independent, and used in web development, data science, automation, AI, and machine learning.",
                "body_html": """<p>Python is a <strong>high-level, interpreted programming language</strong> known for its simplicity and readability. It is designed to be easy to learn for beginners and powerful enough for experienced developers.</p>
<ul>
  <li>Open-source and platform-independent</li>
  <li>Runs on different operating systems without modification</li>
  <li>Used in web development, data science, automation, AI, and machine learning</li>
</ul>"""
            },
            {
                "heading": "Variables and Data Types",
                "summary": "Variables store data and Python automatically determines their type. Common types are int (whole numbers), float (decimals), str (text), and bool (true or false).",
                "body_html": """<p>Variables store data in a program. Python does not require explicit type declaration — it determines the type automatically from the assigned value.</p>
<table>
  <thead><tr><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>int</td><td>Whole numbers</td></tr>
    <tr><td>float</td><td>Decimal numbers</td></tr>
    <tr><td>str</td><td>Text or characters</td></tr>
    <tr><td>bool</td><td>Logical values: true or false</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Input and Output",
                "summary": "Input receives data from the user and output displays results. These operations make programs interactive and are essential for user-facing applications.",
                "body_html": """<p>Input and output operations allow interaction between the user and the program.</p>
<ul>
  <li><strong>Input</strong>: Used to receive data from the user</li>
  <li><strong>Output</strong>: Used to display results or information to the user</li>
</ul>
<p>These operations are essential for making programs interactive.</p>"""
            },
            {
                "heading": "Operators",
                "summary": "Operators perform operations on values. Arithmetic operators handle math, comparison operators compare values and return boolean results, and logical operators combine multiple conditions.",
                "body_html": """<table>
  <thead><tr><th>Type</th><th>Purpose</th></tr></thead>
  <tbody>
    <tr><td>Arithmetic</td><td>Mathematical calculations: addition, subtraction, multiplication, division, modulus, exponentiation</td></tr>
    <tr><td>Comparison</td><td>Compare two values and return a boolean result (true or false)</td></tr>
    <tr><td>Logical</td><td>Combine multiple conditions and return logical results</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Conditional Statements",
                "summary": "Conditional statements control program flow based on conditions. If checks a condition, else runs when it is false, and elif checks multiple conditions in sequence.",
                "body_html": """<p>Conditional statements allow execution of different code blocks based on whether a condition is true or false.</p>
<ul>
  <li><strong>if</strong>: Checks a condition</li>
  <li><strong>else</strong>: Executes when the condition is false</li>
  <li><strong>elif</strong>: Checks multiple conditions in sequence</li>
</ul>
<p>These statements help control the flow of a program.</p>"""
            },
            {
                "heading": "Loops",
                "summary": "Loops execute code repeatedly. For loops are used when the number of iterations is known. While loops continue as long as a condition is true. Loops automate repetitive tasks.",
                "body_html": """<table>
  <thead><tr><th>Loop</th><th>When to Use</th></tr></thead>
  <tbody>
    <tr><td>For Loop</td><td>When the number of iterations is known; used to iterate over a sequence</td></tr>
    <tr><td>While Loop</td><td>When the number of iterations is not known; continues while a condition is true</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Data Structures",
                "summary": "Python has four main data structures: List (ordered, mutable), Tuple (ordered, immutable), Set (unordered, unique values), and Dictionary (key-value pairs).",
                "body_html": """<table>
  <thead><tr><th>Structure</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>List</td><td>Ordered and mutable; items can be added, removed, or modified</td></tr>
    <tr><td>Tuple</td><td>Ordered but immutable; elements cannot be changed after creation</td></tr>
    <tr><td>Set</td><td>Unordered collection of unique elements; duplicates not allowed</td></tr>
    <tr><td>Dictionary</td><td>Collection of key-value pairs for storing related data</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Functions",
                "summary": "Functions are reusable code blocks that perform a specific task. They accept parameters, return results, and can have default values. Lambda functions are small anonymous functions for short operations.",
                "body_html": """<p>Functions are reusable blocks of code that help organize logic and avoid repetition.</p>
<ul>
  <li>Accept inputs (parameters)</li>
  <li>Return outputs (results)</li>
  <li>Can have default values for parameters</li>
  <li><strong>Lambda functions</strong>: Small anonymous functions used for short operations</li>
</ul>"""
            },
            {
                "heading": "Indentation",
                "summary": "Indentation is mandatory in Python and defines the structure of code blocks. Incorrect indentation causes errors, unlike other languages that use braces for block structure.",
                "body_html": """<p>Indentation refers to the spaces at the beginning of a line of code. In Python, indentation is <strong>mandatory</strong> and defines the structure of the program.</p>
<ul>
  <li>Proper indentation ensures correct execution</li>
  <li>Incorrect indentation leads to an <strong>IndentationError</strong></li>
  <li>Python uses indentation instead of braces to define code blocks</li>
</ul>"""
            },
            {
                "heading": "Real-World Application and Conclusion",
                "summary": "Python is used for calculating totals, processing input, and automating workflows. Mastering fundamentals like variables, loops, and functions is essential for data science, ML, and web development.",
                "body_html": """<p>Python is commonly used to perform real-world tasks such as calculating totals, processing user input, and automating workflows. Programs combine variables, functions, and operations to solve practical problems.</p>
<h3>Foundation for Advanced Topics</h3>
<ul>
  <li>Data Science and Machine Learning</li>
  <li>Web Development</li>
  <li>Automation and scripting</li>
</ul>
<p>A strong foundation in these fundamentals helps in writing clean, efficient, and scalable programs.</p>"""
            },
        ],
        "quiz": [
            {"question": "Which Python data structure is ordered and immutable?", "options": ["list", "set", "tuple", "dict"], "answer": 2},
            {"question": "Which function reads user input in Python 3?", "options": ["raw_input()", "input()", "read()", "scan()"], "answer": 1},
            {"question": "What symbol starts a comment in Python?", "options": ["//", "#", "--", "/*"], "answer": 1},
            {"question": "Which data structure stores key-value pairs in Python?", "options": ["list", "tuple", "set", "dictionary"], "answer": 3},
            {"question": "What happens if indentation is incorrect in Python?", "options": ["Nothing", "SyntaxWarning", "IndentationError", "RuntimeError"], "answer": 2},
        ]
    },
    # Python Unit 2
    {
        "title": "Scripting & File Handling",
        "unit_number": 2,
        "content": "Functions and modules, file handling (read/write/append), and exception handling for building practical Python applications.",
        "category": "python",
        "author": "Admin",
        "sections": [
            {
                "heading": "Functions and Modules",
                "summary": "Functions are reusable code blocks that break complex problems into smaller tasks. Modules are collections of related functions grouped in a file, promoting reusability, maintainability, and separation of concerns.",
                "body_html": """<p>Functions are reusable blocks of code designed to perform specific tasks. They help in organizing programs into smaller, manageable parts, making code more readable and maintainable.</p>
<ul>
  <li>Breaking complex problems into smaller tasks</li>
  <li>Reusing logic multiple times</li>
  <li>Improving code clarity and structure</li>
</ul>
<p>Modules are collections of related functions and variables grouped together in a single file.</p>
<table>
  <thead><tr><th>Module Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>Built-in</td><td>Provided by Python by default</td></tr>
    <tr><td>User-defined</td><td>Created by the developer for their program</td></tr>
    <tr><td>External Libraries</td><td>Installed from third-party sources</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "File Handling (Read/Write)",
                "summary": "File handling allows programs to store, retrieve, and manipulate data permanently. Key operations include reading, writing, and appending files. It is essential for storing user data, logs, and reports.",
                "body_html": """<p>File handling refers to the process of working with files stored on a system. It allows programs to store, retrieve, and manipulate data permanently.</p>
<table>
  <thead><tr><th>Operation</th><th>Purpose</th></tr></thead>
  <tbody>
    <tr><td>Reading</td><td>Access stored data from a file</td></tr>
    <tr><td>Writing</td><td>Save new data to a file</td></tr>
    <tr><td>Appending</td><td>Add data without overwriting existing content</td></tr>
    <tr><td>Resource Management</td><td>Properly open and close file resources</td></tr>
  </tbody>
</table>
<p>File handling is essential for applications that need to store user data, logs, reports, or processed results.</p>"""
            },
            {
                "heading": "Exception Handling",
                "summary": "Exception handling manages errors during program execution so the program does not crash. Errors can occur due to invalid input, missing files, or runtime issues. Proper handling improves reliability and debugging.",
                "body_html": """<p>Exception handling is used to manage errors that occur during program execution. It ensures that the program does not crash and can handle unexpected situations gracefully.</p>
<ul>
  <li>Errors can occur due to invalid input, missing files, or runtime issues</li>
  <li>Exception handling allows detection and management of such errors</li>
  <li>Programs can continue execution even after encountering issues</li>
</ul>
<p>Proper exception handling improves reliability, user experience, and debugging.</p>"""
            },
            {
                "heading": "Conclusion",
                "summary": "Scripting and file handling concepts are essential for building practical applications. They allow programs to perform real-world tasks such as data processing, file management, and error handling efficiently.",
                "body_html": """<p>Scripting and file handling concepts are essential for building practical applications. They allow programs to perform real-world tasks such as data processing, file management, and error handling efficiently.</p>"""
            },
        ],
        "quiz": [
            {"question": "What is a module in Python?", "options": ["A loop structure", "A collection of related functions and variables in a file", "A type of variable", "A built-in data type"], "answer": 1},
            {"question": "Which file operation adds data without overwriting existing content?", "options": ["Reading", "Writing", "Appending", "Deleting"], "answer": 2},
            {"question": "What is the purpose of exception handling?", "options": ["Speed up execution", "Manage errors so the program does not crash", "Delete unused variables", "Import modules"], "answer": 1},
            {"question": "Which type of module is installed from third-party sources?", "options": ["Built-in", "User-defined", "External Library", "System module"], "answer": 2},
            {"question": "What does file handling allow a program to do?", "options": ["Run faster", "Store and retrieve data permanently", "Create user interfaces", "Handle network requests"], "answer": 1},
        ]
    },
    # Python Unit 3
    {
        "title": "Introduction to Machine Learning",
        "unit_number": 3,
        "content": "Introduction to machine learning, NumPy and Pandas basics, data preprocessing, simple ML models (linear regression, classification), and importance of ML.",
        "category": "python",
        "author": "Admin",
        "sections": [
            {
                "heading": "Introduction to Machine Learning",
                "summary": "Machine Learning is a branch of AI that enables systems to learn from data and improve without being explicitly programmed. It identifies patterns, makes predictions, and is used in recommendations, image recognition, and fraud detection.",
                "body_html": """<p>Machine Learning is a branch of <strong>artificial intelligence</strong> that enables systems to learn from data and improve performance without being explicitly programmed.</p>
<p>It focuses on building models that can identify patterns, make predictions, and support decision-making.</p>
<ul>
  <li>Recommendation systems</li>
  <li>Image and speech recognition</li>
  <li>Fraud detection</li>
  <li>Data analysis</li>
</ul>"""
            },
            {
                "heading": "NumPy and Pandas Basics",
                "summary": "NumPy handles numerical computations and efficient array operations. Pandas works with structured data for cleaning, transformation, and analysis. Both libraries form the foundation for working with datasets in machine learning.",
                "body_html": """<table>
  <thead><tr><th>Library</th><th>Purpose</th><th>Key Use</th></tr></thead>
  <tbody>
    <tr><td>NumPy</td><td>Numerical computations</td><td>Efficient handling of arrays and mathematical operations</td></tr>
    <tr><td>Pandas</td><td>Structured data analysis</td><td>Data cleaning, transformation, and analysis</td></tr>
  </tbody>
</table>
<p>These libraries form the foundation for working with datasets in machine learning.</p>"""
            },
            {
                "heading": "Data Preprocessing",
                "summary": "Data preprocessing prepares raw data before applying ML models. Key steps include cleaning data, converting formats, scaling values, and selecting relevant features. Proper preprocessing improves model accuracy.",
                "body_html": """<p>Data preprocessing is the process of preparing raw data before applying machine learning models.</p>
<table>
  <thead><tr><th>Step</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>Cleaning</td><td>Removing errors or missing values from data</td></tr>
    <tr><td>Formatting</td><td>Converting data into a suitable format</td></tr>
    <tr><td>Scaling</td><td>Normalizing values for consistent ranges</td></tr>
    <tr><td>Feature Selection</td><td>Selecting the most relevant attributes</td></tr>
  </tbody>
</table>
<p>Proper preprocessing improves model accuracy and performance.</p>"""
            },
            {
                "heading": "Simple Machine Learning Models",
                "summary": "Linear Regression predicts continuous values based on variable relationships, used for forecasting. Classification categorizes data into groups, used in spam detection and image classification.",
                "body_html": """<table>
  <thead><tr><th>Model</th><th>Purpose</th><th>Common Use</th></tr></thead>
  <tbody>
    <tr><td>Linear Regression</td><td>Predict continuous values based on variable relationships</td><td>Forecasting and trend analysis</td></tr>
    <tr><td>Classification</td><td>Categorize data into different classes or groups</td><td>Spam detection and image classification</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Importance and Conclusion",
                "summary": "Machine Learning enables data-driven decisions, automates complex tasks, and improves efficiency. Understanding preprocessing and basic models is essential before moving to advanced algorithms and real-world applications.",
                "body_html": """<h3>Importance of Machine Learning</h3>
<ul>
  <li>Enables data-driven decision making</li>
  <li>Automates complex tasks</li>
  <li>Improves efficiency and accuracy</li>
  <li>Widely used in modern technologies</li>
</ul>
<h3>Conclusion</h3>
<p>Introduction to Machine Learning provides the foundation for understanding how systems learn from data. Concepts like data preprocessing and basic models are essential before moving to advanced algorithms and real-world applications.</p>"""
            },
        ],
        "quiz": [
            {"question": "What is Machine Learning?", "options": ["A programming language", "A branch of AI that enables systems to learn from data", "A database system", "A web framework"], "answer": 1},
            {"question": "Which library is used for numerical computations in Python?", "options": ["Pandas", "Matplotlib", "NumPy", "Scikit-learn"], "answer": 2},
            {"question": "What is the purpose of data preprocessing?", "options": ["Train the model directly", "Prepare raw data before applying ML models", "Visualize results", "Deploy applications"], "answer": 1},
            {"question": "Which ML model is used to predict continuous values?", "options": ["Classification", "Clustering", "Linear Regression", "Decision Tree"], "answer": 2},
            {"question": "Which library is used for data cleaning and transformation in Python?", "options": ["NumPy", "Pandas", "Flask", "TensorFlow"], "answer": 1},
        ]
    },
    # React
    {
        "title": "React Core Concepts",
        "unit_number": 1,
        "content": "Introduction to React, setting up a React app, JSX syntax, functional and class components, rendering elements, props and component reusability.",
        "category": "react",
        "author": "Admin",
        "sections": [
            {
                "heading": "Introduction to React",
                "summary": "React is a JavaScript library by Meta for building user interfaces. It is component-based, uses a Virtual DOM for performance, and powers apps like Facebook and Instagram.",
                "body_html": """<p>React is a <strong>JavaScript library</strong> developed by Facebook (Meta) for building user interfaces, especially for web applications. It focuses on creating reusable UI components and managing the user interface efficiently.</p>
<p>React is widely used in modern web development due to its performance, flexibility, and strong ecosystem. Many popular applications like Facebook and Instagram are built using React.</p>"""
            },
            {
                "heading": "Key Features of React",
                "summary": "React uses component-based architecture for reusability, a Virtual DOM for efficient rendering, and updates only changed elements, making applications faster and easier to maintain.",
                "body_html": """<table>
  <thead><tr><th>Feature</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>Component-Based Architecture</td><td>Applications are built using independent and reusable components</td></tr>
    <tr><td>Virtual DOM</td><td>A virtual representation of the DOM that updates only necessary parts of the UI</td></tr>
    <tr><td>Reusability</td><td>Components can be reused across different parts of the application</td></tr>
    <tr><td>Efficient Rendering</td><td>Only changed elements are updated, making applications faster</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Setting Up React",
                "summary": "React apps are created using setup tools that manage dependencies and configuration. Traditional tools help beginners get started quickly, while modern tools offer faster development environments.",
                "body_html": """<p>React applications can be created using modern tools that simplify development.</p>
<ul>
  <li><strong>Traditional setup tools</strong>: Help beginners quickly start a project</li>
  <li><strong>Modern tools</strong>: Provide faster development environments and better performance</li>
</ul>
<p>These tools manage dependencies, configuration, and development servers, allowing developers to focus on building applications.</p>"""
            },
            {
                "heading": "JSX (JavaScript XML)",
                "summary": "JSX is a syntax extension that allows writing HTML-like structures in JavaScript. It requires a single parent element, supports dynamic values, and uses special naming conventions for attributes.",
                "body_html": """<p>JSX is a syntax extension that allows writing HTML-like structures within JavaScript. It makes the code more readable and easier to understand.</p>
<ul>
  <li>Allows embedding dynamic values inside UI elements</li>
  <li>Requires a single parent element for proper rendering</li>
  <li>Uses special naming conventions for attributes</li>
</ul>
<p>JSX plays a crucial role in defining the structure of user interfaces in React.</p>"""
            },
            {
                "heading": "Components",
                "summary": "Components are the building blocks of React. Functional components are modern, simple, and preferred. Class components are the older approach used before modern React features were introduced.",
                "body_html": """<p>Components are the building blocks of a React application. Each component represents a part of the user interface.</p>
<table>
  <thead><tr><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>Functional Components</td><td>Modern and widely used; simple functions that return UI</td></tr>
    <tr><td>Class Components</td><td>Older approach used before the introduction of modern features</td></tr>
  </tbody>
</table>
<p>Functional components are preferred in modern development due to simplicity and better performance.</p>"""
            },
            {
                "heading": "Props (Properties)",
                "summary": "Props pass data from one component to another. They are read-only, allow component customization, and enable communication between components to make them dynamic and reusable.",
                "body_html": """<p>Props are used to pass data from one component to another. They help in making components dynamic and reusable.</p>
<ul>
  <li>Props are <strong>read-only</strong></li>
  <li>They allow customization of components</li>
  <li>They enable communication between components</li>
</ul>"""
            },
            {
                "heading": "Event Handling",
                "summary": "React handles user interactions like clicks and form submissions using predefined event methods with camelCase naming. Functions define the event behavior to create interactive interfaces.",
                "body_html": """<p>React allows handling user interactions such as clicks, inputs, and form submissions.</p>
<ul>
  <li>Events are handled using predefined methods</li>
  <li>Event names follow a specific naming convention (camelCase)</li>
  <li>Functions are used to define event behavior</li>
</ul>
<p>Event handling enables interactive and responsive user interfaces.</p>"""
            },
            {
                "heading": "Conditional Rendering",
                "summary": "Conditional rendering displays different content based on conditions. It is used for authentication, loading states, and user roles, allowing the UI to change dynamically based on application state.",
                "body_html": """<p>Conditional rendering allows displaying different content based on certain conditions.</p>
<ul>
  <li>UI changes dynamically based on application state</li>
  <li>Conditions determine what is shown to the user</li>
  <li>Useful for authentication, loading states, and user roles</li>
</ul>"""
            },
            {
                "heading": "Lists and Keys",
                "summary": "React renders lists of elements dynamically. Keys are unique identifiers assigned to each list element that help React track changes and optimize updates efficiently.",
                "body_html": """<p>React allows rendering lists of elements dynamically.</p>
<ul>
  <li>Lists are used to display multiple items efficiently</li>
  <li><strong>Keys</strong> are unique identifiers assigned to each element</li>
  <li>Keys help React track changes and optimize updates</li>
</ul>"""
            },
            {
                "heading": "Best Practices and Conclusion",
                "summary": "Use functional components, keep them small and focused, use meaningful names, never modify props directly, and always use unique keys for lists. These fundamentals are the foundation for advanced React topics.",
                "body_html": """<h3>Best Practices</h3>
<ul>
  <li>Use functional components for better readability and performance</li>
  <li>Keep components small and focused on a single task</li>
  <li>Use meaningful and descriptive component names</li>
  <li>Avoid modifying props directly to maintain data integrity</li>
  <li>Always use unique identifiers when rendering lists</li>
</ul>
<p>Mastering these basics is essential before moving to advanced topics such as state management, hooks, routing, and full-stack development.</p>"""
            },
        ],
        "quiz": [
            {"question": "What does JSX stand for?", "options": ["JavaScript XML", "Java Syntax Extension", "JSON XML", "JavaScript Extra"], "answer": 0},
            {"question": "How is data passed from parent to child in React?", "options": ["state", "props", "context", "refs"], "answer": 1},
            {"question": "Which command creates a new React app?", "options": ["npm init react", "npx create-react-app", "react new app", "npm react start"], "answer": 1},
            {"question": "Which type of React component is preferred in modern development?", "options": ["Class component", "Functional component", "Pure component", "HOC"], "answer": 1},
            {"question": "What is the Virtual DOM in React?", "options": ["A real browser DOM", "A copy of the database", "A virtual representation of the UI for efficient updates", "A CSS framework"], "answer": 2},
        ]
    },
    # React Unit 2
    {
        "title": "Hooks & State Management",
        "unit_number": 2,
        "content": "React Hooks: useState, useEffect, props vs state, state management, and event handling in functional components.",
        "category": "react",
        "author": "Admin",
        "sections": [
            {
                "heading": "Introduction to Hooks",
                "summary": "Hooks are special features in React that allow developers to use state and other functionalities in functional components. They simplify component logic and eliminate the need for class components in most cases.",
                "body_html": """<p>Hooks are special features in React that allow developers to use state and other functionalities in functional components. They simplify component logic and eliminate the need for class components in most cases.</p>
<p>Hooks make code more readable, reusable, and easier to manage, especially in large applications.</p>"""
            },
            {
                "heading": "useState",
                "summary": "useState manages state in functional components. State is dynamic data that changes over time and triggers re-renders. It is used for user input, toggling UI elements, and managing application data.",
                "body_html": """<p>useState is a hook used to manage state in functional components. State represents dynamic data that can change over time and affects how the user interface is rendered.</p>
<ul>
  <li>Allows components to store and update data</li>
  <li>When state changes, the component automatically re-renders</li>
  <li>Helps create interactive and dynamic user interfaces</li>
</ul>
<p>State is commonly used for handling user input, toggling UI elements, and managing application data.</p>"""
            },
            {
                "heading": "useEffect",
                "summary": "useEffect handles side effects like fetching data, updating the DOM, and setting timers. It runs after rendering and can be controlled to run only when specific data changes, replacing class lifecycle methods.",
                "body_html": """<p>useEffect is a hook used to handle side effects in a component. Side effects are operations that occur outside the normal rendering process.</p>
<table>
  <thead><tr><th>Concept</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>When it runs</td><td>After the component renders</td></tr>
    <tr><td>Controlled execution</td><td>Can run only when specific data changes</td></tr>
    <tr><td>Replaces</td><td>Lifecycle methods used in older class components</td></tr>
  </tbody>
</table>
<p>Examples of side effects: fetching data from APIs, updating the DOM, setting up timers, subscribing to external services.</p>"""
            },
            {
                "heading": "Props and State",
                "summary": "Props are passed from parent to child, read-only, and make components reusable. State is managed within a component, can be updated, and controls rendering. Props are external and immutable; state is internal and mutable.",
                "body_html": """<table>
  <thead><tr><th>Concept</th><th>Source</th><th>Mutable</th><th>Purpose</th></tr></thead>
  <tbody>
    <tr><td>Props</td><td>Parent component</td><td>No (read-only)</td><td>Make components reusable and dynamic</td></tr>
    <tr><td>State</td><td>Within component</td><td>Yes</td><td>Control component behavior and rendering</td></tr>
  </tbody>
</table>
<p>Props are external and immutable, while state is internal and mutable.</p>"""
            },
            {
                "heading": "State Management",
                "summary": "State management handles how data is shared within an application. Local state is managed within components. Shared state uses props or advanced tools. Proper management ensures consistency and predictable behavior.",
                "body_html": """<p>State management refers to how data is handled and shared within an application.</p>
<ul>
  <li>Local state is managed within individual components</li>
  <li>Shared state can be passed through props or managed using advanced tools</li>
  <li>Proper state management ensures consistency and predictable behavior</li>
</ul>
<p>Efficient state management is essential for building scalable React applications.</p>"""
            },
            {
                "heading": "Event Handling",
                "summary": "Event handling allows React apps to respond to user interactions like clicks, typing, and form submissions. Events trigger functions that update state or perform actions, enabling interactive and responsive interfaces.",
                "body_html": """<p>Event handling in React allows applications to respond to user interactions such as clicks, typing, and form submissions.</p>
<ul>
  <li>Events trigger functions that update state or perform actions</li>
  <li>Event handling enables interactivity</li>
  <li>Essential for creating responsive user interfaces</li>
</ul>
<p>React provides a structured way to manage events, ensuring consistency across browsers.</p>"""
            },
            {
                "heading": "Best Practices and Conclusion",
                "summary": "Use hooks to simplify logic, keep state minimal, avoid unnecessary re-renders, and maintain clear data flow. Hooks and state management are essential for building dynamic and interactive React applications.",
                "body_html": """<h3>Best Practices</h3>
<ul>
  <li>Use hooks to simplify component logic</li>
  <li>Keep state minimal and only store necessary data</li>
  <li>Avoid unnecessary re-renders by managing dependencies properly</li>
  <li>Separate logic into reusable components</li>
  <li>Maintain clear data flow between components</li>
</ul>
<p>Hooks and state management are essential for building dynamic and interactive React applications. Understanding how to manage data and handle side effects is key to developing modern user interfaces.</p>"""
            },
        ],
        "quiz": [
            {"question": "What is the purpose of the useState hook?", "options": ["Fetch data from APIs", "Manage state in functional components", "Handle routing", "Style components"], "answer": 1},
            {"question": "What does useEffect handle in React?", "options": ["Component styling", "Side effects like data fetching and DOM updates", "Routing between pages", "Form validation"], "answer": 1},
            {"question": "Which of the following is true about props?", "options": ["They are mutable", "They are managed within the component", "They are read-only and passed from parent to child", "They replace state"], "answer": 2},
            {"question": "What triggers a component to re-render in React?", "options": ["Changing a prop from inside the component", "A state change", "Adding a new CSS class", "Importing a module"], "answer": 1},
            {"question": "Which hook replaces lifecycle methods in class components?", "options": ["useState", "useRef", "useEffect", "useContext"], "answer": 2},
        ]
    },
    # React Unit 3
    {
        "title": "UI Development",
        "unit_number": 3,
        "content": "UI development in React: styling approaches, forms, form validation, and routing for building complete user interfaces.",
        "category": "react",
        "author": "Admin",
        "sections": [
            {
                "heading": "Introduction to UI Development in React",
                "summary": "UI development in React focuses on designing visually appealing and user-friendly interfaces. It involves styling components, handling user input, and navigating between views to improve user experience.",
                "body_html": """<p>UI development in React focuses on designing and building visually appealing and user-friendly interfaces. It involves styling components, handling user input, and navigating between different views.</p>
<p>A well-designed UI improves user experience and makes applications more intuitive.</p>"""
            },
            {
                "heading": "Styling in React",
                "summary": "React supports traditional CSS for global or scoped styles and modern utility-first styling for rapid development. Consistent styling ensures responsive layouts and visually attractive applications.",
                "body_html": """<table>
  <thead><tr><th>Approach</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>CSS Styling</td><td>Traditional CSS applied globally or scoped to specific components</td></tr>
    <tr><td>Utility-First Styling</td><td>Predefined classes for rapid UI development</td></tr>
  </tbody>
</table>
<ul>
  <li>Separation of structure and design</li>
  <li>Consistent design patterns</li>
  <li>Responsive layouts for different devices</li>
</ul>"""
            },
            {
                "heading": "Forms in React",
                "summary": "Forms collect user input like text and selections. Input data is managed through state. Forms are essential for login systems, registrations, and data submission in React applications.",
                "body_html": """<p>Forms are used to collect user input such as text, selections, and user data.</p>
<ul>
  <li>Forms consist of input fields, buttons, and validation rules</li>
  <li>Data entered by users is managed through state</li>
  <li>Forms enable interaction between users and applications</li>
</ul>
<p>Forms are essential for features like login systems, registrations, and data submission.</p>"""
            },
            {
                "heading": "Form Validation",
                "summary": "Validation ensures user input meets requirements before processing. It prevents invalid submissions, improves data accuracy, and provides feedback to users when errors occur.",
                "body_html": """<p>Validation ensures that user input meets specific requirements before being processed.</p>
<ul>
  <li>Prevents invalid or incomplete data submission</li>
  <li>Improves data accuracy and reliability</li>
  <li>Provides feedback to users when errors occur</li>
</ul>
<p>Validation enhances user experience and ensures application reliability.</p>"""
            },
            {
                "heading": "Routing (Navigation)",
                "summary": "Routing navigates between pages or views without reloading. It enables single-page application behavior, maps URLs to components, and allows smooth transitions between views.",
                "body_html": """<p>Routing is used to navigate between different pages or views in a React application without reloading the page.</p>
<ul>
  <li>Enables single-page application behavior</li>
  <li>Maps different URLs to specific components</li>
  <li>Allows smooth transitions between views</li>
</ul>
<p>Routing is essential for building multi-page-like experiences within a single application.</p>"""
            },
            {
                "heading": "Best Practices and Conclusion",
                "summary": "Keep UI components simple and reusable, use consistent styling, validate input, ensure responsive design, and organize components logically. Mastering styling, forms, and routing is essential for professional React apps.",
                "body_html": """<h3>Best Practices</h3>
<ul>
  <li>Keep UI components simple and reusable</li>
  <li>Use consistent styling across the application</li>
  <li>Validate user input properly</li>
  <li>Ensure responsive design for different devices</li>
  <li>Organize components logically</li>
</ul>
<p>UI Development in React focuses on creating engaging, user-friendly interfaces. Mastering styling, forms, validation, and routing is essential for building complete and professional web applications.</p>"""
            },
        ],
        "quiz": [
            {"question": "What is the purpose of routing in React?", "options": ["Style components", "Manage state", "Navigate between views without reloading the page", "Fetch data from APIs"], "answer": 2},
            {"question": "How is user input from forms managed in React?", "options": ["Through props", "Through state", "Through routing", "Through CSS"], "answer": 1},
            {"question": "What does form validation do?", "options": ["Styles the form", "Submits data automatically", "Prevents invalid data submission and provides feedback", "Fetches data from a server"], "answer": 2},
            {"question": "Which styling approach uses predefined classes for rapid UI development?", "options": ["Inline CSS", "CSS Modules", "Utility-First Styling", "Global CSS"], "answer": 2},
            {"question": "What is a key benefit of single-page application routing?", "options": ["Reloads the page on every navigation", "Allows smooth transitions without full page reloads", "Removes the need for components", "Disables form validation"], "answer": 1},
        ]
    },
    # Node.js
    {
        "title": "Node.js Basics",
        "unit_number": 1,
        "content": "Introduction to Node.js, Node.js architecture, installing Node & npm, built-in and custom modules, the File System module, and event-driven programming.",
        "category": "nodejs",
        "author": "Admin",
        "sections": [
            {
                "heading": "Introduction to Node.js",
                "summary": "Node.js is a runtime environment that allows JavaScript to run outside the browser. It is built on a powerful engine for fast execution and is designed for scalable, high-performance server-side applications.",
                "body_html": """<p>Node.js is a <strong>runtime environment</strong> that allows JavaScript to be executed outside the browser. It is built on a powerful engine that enables fast and efficient execution of JavaScript code.</p>
<p>Node.js is designed for building scalable and high-performance applications, especially server-side and network-based systems. It uses an <strong>event-driven, non-blocking architecture</strong>, which makes it suitable for handling multiple requests simultaneously without slowing down performance.</p>
<p>It is widely used for developing web servers, APIs, real-time applications, and backend services.</p>"""
            },
            {
                "heading": "Key Features of Node.js",
                "summary": "Node.js uses asynchronous non-blocking I/O making it lightweight and efficient. It supports event-driven architecture, is highly scalable for real-time applications, and has a large ecosystem of libraries.",
                "body_html": """<p>Node.js offers several important features that make it popular among developers:</p>
<ul>
  <li>Uses <strong>asynchronous programming</strong>, allowing multiple operations to run without waiting for each other</li>
  <li>Lightweight and efficient</li>
  <li>Supports <strong>event-driven architecture</strong></li>
  <li>Highly scalable and suitable for real-time applications</li>
  <li>Has a large ecosystem of libraries and tools</li>
</ul>"""
            },
            {
                "heading": "Node Modules",
                "summary": "Node.js follows a modular approach where applications are divided into reusable modules. There are three types: built-in modules provided by Node.js, user-defined modules created by developers, and third-party modules installed externally.",
                "body_html": """<p>Node.js follows a <strong>modular approach</strong>, where applications are divided into smaller, reusable pieces called modules.</p>
<table>
  <thead><tr><th>Module Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>Built-in Modules</td><td>Provided by Node.js itself (e.g. fs, http, path)</td></tr>
    <tr><td>User-defined Modules</td><td>Created by developers for their own application</td></tr>
    <tr><td>Third-party Modules</td><td>Installed from external sources via npm</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Importance of Modules",
                "summary": "Modules promote code reusability, help organize large applications, reduce duplication, and make debugging easier. Breaking applications into smaller parts helps developers manage complexity better.",
                "body_html": """<p>Modules play a crucial role in Node.js development because they:</p>
<ul>
  <li>Promote <strong>code reusability</strong></li>
  <li>Help in organizing large applications</li>
  <li>Reduce code duplication</li>
  <li>Make debugging and maintenance easier</li>
</ul>
<p>By breaking applications into smaller parts, developers can work more efficiently and manage complexity better.</p>"""
            },
            {
                "heading": "File System in Node.js",
                "summary": "The file system module allows Node.js to interact with files — creating, reading, updating, and deleting them. File operations are handled asynchronously so the program continues executing while files are being processed.",
                "body_html": """<p>The <strong>file system</strong> is an important part of Node.js that allows interaction with files stored on a computer.</p>
<p>Node.js provides features to create, read, update, and delete files. It also allows working with directories and managing file structures.</p>
<p>File operations in Node.js are typically handled <strong>asynchronously</strong>, which means the program can continue executing other tasks while file operations are being processed.</p>"""
            },
            {
                "heading": "File Handling Concepts",
                "summary": "Node.js supports reading, writing, appending, deleting files and managing directories. These operations are essential for applications that need to store, retrieve, or process data.",
                "body_html": """<p>Node.js supports various file-related operations such as:</p>
<ul>
  <li>Reading data from files</li>
  <li>Writing data to files</li>
  <li>Appending content to existing files</li>
  <li>Deleting files</li>
  <li>Managing directories</li>
</ul>"""
            },
            {
                "heading": "Advantages and Conclusion",
                "summary": "Node.js offers efficient handling of large files, non-blocking operations for better performance, and easy integration with backend systems. These fundamentals are the foundation for building servers, APIs, and database-driven applications.",
                "body_html": """<h3>Advantages of Using File System in Node.js</h3>
<ul>
  <li>Efficient handling of large files</li>
  <li>Non-blocking operations improve performance</li>
  <li>Suitable for real-time and data-driven applications</li>
  <li>Easy integration with backend systems</li>
</ul>
<h3>Conclusion</h3>
<p>Node.js Basics provide the foundation for backend development using JavaScript. Understanding concepts like modules and file systems helps in building scalable and efficient applications.</p>"""
            },
        ],
        "quiz": [
            {"question": "What is npm?", "options": ["Node Package Manager", "New Project Manager", "Node Process Module", "None"], "answer": 0},
            {"question": "Which module handles file operations in Node.js?", "options": ["path", "os", "fs", "http"], "answer": 2},
            {"question": "Node.js is built on which JavaScript engine?", "options": ["SpiderMonkey", "V8", "Chakra", "Hermes"], "answer": 1},
            {"question": "Node.js uses which I/O model?", "options": ["Multi-threaded blocking", "Event-driven non-blocking", "Synchronous blocking", "Process-based"], "answer": 1},
            {"question": "Which command initializes a new Node.js project?", "options": ["node start", "npm init", "node init", "npm create"], "answer": 1},
        ]
    },
    # Node.js Unit 2
    {
        "title": "Server & APIs",
        "unit_number": 2,
        "content": "Creating HTTP servers in Node.js, REST APIs, HTTP methods, JSON data exchange, and Express.js basics.",
        "category": "nodejs",
        "author": "Admin",
        "sections": [
            {
                "heading": "Introduction to Servers in Node.js",
                "summary": "A server listens for client requests and responds with data or services. Node.js is widely used for servers due to its non-blocking, event-driven architecture that handles multiple requests efficiently.",
                "body_html": """<p>A server is a system that listens for requests from clients and responds with the requested data or services. In web development, servers handle communication between the frontend (client) and backend systems.</p>
<p>Node.js is widely used to create servers because of its <strong>non-blocking, event-driven architecture</strong>, which allows it to handle multiple requests efficiently.</p>"""
            },
            {
                "heading": "Creating a Server with HTTP",
                "summary": "Node.js can create web servers that listen on a specific port, process incoming requests, and send responses using the HTTP protocol. This forms the foundation of backend development.",
                "body_html": """<p>Node.js provides the ability to create web servers that can handle incoming requests and send responses.</p>
<ul>
  <li>A server listens on a specific port for incoming requests</li>
  <li>It processes requests and sends appropriate responses</li>
  <li>Communication happens using the <strong>HTTP protocol</strong></li>
</ul>
<p>This forms the foundation of backend development, enabling applications to serve web pages and data.</p>"""
            },
            {
                "heading": "REST APIs",
                "summary": "REST APIs are a standard way to design networked applications. They expose endpoints accessed by clients using HTTP methods, with data exchanged in JSON format between frontend and backend systems.",
                "body_html": """<p>REST (Representational State Transfer) APIs are a standard way of designing networked applications. They allow communication between client and server using structured requests.</p>
<ul>
  <li>APIs expose endpoints that clients can access</li>
  <li>Different operations are performed using standard HTTP methods</li>
  <li>Data is usually exchanged in a structured format like <strong>JSON</strong></li>
</ul>
<p>REST APIs are widely used in modern applications for data exchange between frontend and backend systems.</p>"""
            },
            {
                "heading": "Importance of REST APIs",
                "summary": "REST APIs enable communication between different systems, allow separation of frontend and backend, make applications scalable and flexible, and support integration with external services.",
                "body_html": """<ul>
  <li>Enable communication between different systems</li>
  <li>Allow separation of frontend and backend</li>
  <li>Make applications scalable and flexible</li>
  <li>Support integration with external services</li>
</ul>"""
            },
            {
                "heading": "Express.js Basics",
                "summary": "Express.js is a lightweight framework built on Node.js that simplifies server and API development. It handles routes and requests easily, supports middleware, and is widely used for building scalable backend services.",
                "body_html": """<p>Express.js is a lightweight framework built on top of Node.js that simplifies server and API development.</p>
<ul>
  <li>Provides a simple way to handle routes and requests</li>
  <li>Reduces complexity compared to using core Node.js features</li>
  <li>Supports middleware for additional functionality</li>
  <li>Helps in building robust and scalable applications</li>
</ul>
<p>Express.js is widely used for developing APIs and backend services due to its simplicity and flexibility.</p>"""
            },
            {
                "heading": "Conclusion",
                "summary": "Understanding servers and APIs is essential for backend development. HTTP servers, REST APIs, and Express.js simplify building scalable and efficient web applications.",
                "body_html": """<p>Understanding servers and APIs is essential for backend development. Concepts like HTTP servers, REST APIs, and frameworks simplify the process of building scalable and efficient web applications.</p>"""
            },
        ],
        "quiz": [
            {"question": "What is the role of a server in web development?", "options": ["Style web pages", "Listen for client requests and respond with data", "Manage CSS files", "Store images"], "answer": 1},
            {"question": "What does REST stand for?", "options": ["Remote Execution State Transfer", "Representational State Transfer", "Request and Response Technology", "Reliable Server Transfer"], "answer": 1},
            {"question": "What format is commonly used to exchange data in REST APIs?", "options": ["XML", "CSV", "JSON", "HTML"], "answer": 2},
            {"question": "What is Express.js?", "options": ["A database system", "A frontend framework", "A lightweight Node.js framework for server and API development", "A CSS library"], "answer": 2},
            {"question": "What does a server listen on to receive incoming requests?", "options": ["A file path", "A database", "A specific port", "A CSS class"], "answer": 2},
        ]
    },
    # Node.js Unit 3
    {
        "title": "Advanced Backend",
        "unit_number": 3,
        "content": "Middleware, JWT authentication, error handling, and best practices for building secure and scalable Node.js backend applications.",
        "category": "nodejs",
        "author": "Admin",
        "sections": [
            {
                "heading": "Middleware",
                "summary": "Middleware functions act as intermediaries in the request-response cycle. They process requests before reaching the final handler and are used for logging, parsing data, authentication, and error handling.",
                "body_html": """<p>Middleware refers to functions that act as intermediaries in the request-response cycle of a server.</p>
<ul>
  <li>Middleware processes requests before they reach the final handler</li>
  <li>It can modify requests, responses, or perform additional operations</li>
  <li>Multiple middleware functions can be used in sequence</li>
</ul>
<table>
  <thead><tr><th>Common Use</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>Logging</td><td>Recording incoming requests for monitoring</td></tr>
    <tr><td>Parsing</td><td>Converting request data into usable formats</td></tr>
    <tr><td>Authentication</td><td>Verifying user identity before processing</td></tr>
    <tr><td>Error Handling</td><td>Managing errors in a centralized way</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Authentication (JWT)",
                "summary": "JWT is a popular stateless authentication method. After login, a token is generated and sent to the client. The client uses it for future requests and the server verifies it to grant access.",
                "body_html": """<p>Authentication is the process of verifying the identity of a user. JWT (JSON Web Token) is a popular method used for authentication in modern applications.</p>
<table>
  <thead><tr><th>Step</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>Login</td><td>User provides credentials; server verifies them</td></tr>
    <tr><td>Token Generation</td><td>Server generates a JWT and sends it to the client</td></tr>
    <tr><td>Request</td><td>Client sends the token with future requests</td></tr>
    <tr><td>Verification</td><td>Server verifies the token to grant access</td></tr>
  </tbody>
</table>
<ul>
  <li>Stateless authentication — no need to store sessions</li>
  <li>Secure and scalable</li>
  <li>Widely used in APIs and web applications</li>
</ul>"""
            },
            {
                "heading": "Error Handling",
                "summary": "Error handling manages errors during application execution to prevent crashes. Errors can occur from invalid input, server issues, or external failures. Proper handling improves stability and user experience.",
                "body_html": """<p>Error handling is the process of managing errors that occur during application execution.</p>
<ul>
  <li>Errors can occur due to invalid input, server issues, or external failures</li>
  <li>Proper handling prevents application crashes</li>
  <li>Provides meaningful responses to users</li>
  <li>Improves application stability and simplifies debugging</li>
</ul>"""
            },
            {
                "heading": "Best Practices and Conclusion",
                "summary": "Use middleware for modular design, implement secure authentication, handle errors consistently, keep backend logic organized, and follow proper API design principles for robust backend systems.",
                "body_html": """<h3>Best Practices</h3>
<ul>
  <li>Use middleware effectively for modular design</li>
  <li>Implement secure authentication mechanisms</li>
  <li>Handle errors gracefully and consistently</li>
  <li>Keep backend logic organized and scalable</li>
  <li>Follow proper API design principles</li>
</ul>
<h3>Conclusion</h3>
<p>Advanced backend concepts focus on building secure, scalable, and maintainable applications. Middleware, authentication, and error handling are critical for creating robust backend systems.</p>"""
            },
        ],
        "quiz": [
            {"question": "What is the role of middleware in Node.js?", "options": ["Style the frontend", "Act as intermediary functions in the request-response cycle", "Store data in a database", "Render HTML pages"], "answer": 1},
            {"question": "What does JWT stand for?", "options": ["Java Web Token", "JSON Web Token", "JavaScript Web Transfer", "JSON Web Transfer"], "answer": 1},
            {"question": "What is a key advantage of JWT authentication?", "options": ["Requires server-side session storage", "Only works with SQL databases", "Stateless — no need to store sessions on the server", "Only used for frontend apps"], "answer": 2},
            {"question": "What does error handling prevent in a Node.js application?", "options": ["Slow rendering", "Application crashes due to unhandled errors", "CSS conflicts", "Database creation"], "answer": 1},
            {"question": "Which of the following is a common use of middleware?", "options": ["Styling components", "Managing CSS files", "Logging and authentication checks", "Creating database schemas"], "answer": 2},
        ]
    },
    # Databases
    {
        "title": "SQL Fundamentals",
        "unit_number": 1,
        "content": "Introduction to DBMS & RDBMS, tables/rows/columns, SQL commands (SELECT/INSERT/UPDATE/DELETE), constraints (primary key, foreign key), joins (inner/left/right), and aggregate functions.",
        "category": "databases",
        "author": "Admin",
        "sections": [
            {
                "heading": "Introduction to SQL",
                "summary": "SQL is the standard language for interacting with relational databases. It is used to store, retrieve, update, and manage data in software, banking, analytics, and enterprise systems.",
                "body_html": """<p>SQL (Structured Query Language) is a standard language used to interact with relational databases. It acts as a bridge between users and databases.</p>
<ul>
  <li>Store and retrieve data efficiently</li>
  <li>Update and manage records</li>
  <li>Used in software development, banking, data analysis, and enterprise applications</li>
</ul>"""
            },
            {
                "heading": "What is a Database?",
                "summary": "A database is an organized collection of data that can be easily accessed and managed. Relational databases store data in structured tables, while NoSQL databases use flexible formats.",
                "body_html": """<p>A database is an organized collection of data designed for efficient retrieval and manipulation.</p>
<table>
  <thead><tr><th>Type</th><th>Description</th><th>Examples</th></tr></thead>
  <tbody>
    <tr><td>Relational (RDBMS)</td><td>Data stored in tables using SQL</td><td>MySQL, PostgreSQL</td></tr>
    <tr><td>Non-Relational (NoSQL)</td><td>Flexible formats for unstructured data</td><td>MongoDB</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Structure of a Relational Database",
                "summary": "A relational database organizes data into tables with rows and columns. Each table represents an entity like students or products, with rows as records and columns as attributes.",
                "body_html": """<p>A relational database consists of:</p>
<table>
  <thead><tr><th>Term</th><th>Meaning</th></tr></thead>
  <tbody>
    <tr><td>Table</td><td>Organized collection of data for one entity</td></tr>
    <tr><td>Row (Tuple)</td><td>A single record</td></tr>
    <tr><td>Column (Attribute)</td><td>A property of the data</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "SQL Command Categories",
                "summary": "SQL commands are grouped into DDL (define structure), DML (manipulate data), DQL (query data), and DCL (control access). Each category serves a distinct purpose.",
                "body_html": """<table>
  <thead><tr><th>Category</th><th>Full Form</th><th>Purpose</th></tr></thead>
  <tbody>
    <tr><td>DDL</td><td>Data Definition Language</td><td>Define and modify database structure</td></tr>
    <tr><td>DML</td><td>Data Manipulation Language</td><td>Insert, update, and delete data</td></tr>
    <tr><td>DQL</td><td>Data Query Language</td><td>Retrieve data from the database</td></tr>
    <tr><td>DCL</td><td>Data Control Language</td><td>Control access and permissions</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Constraints in SQL",
                "summary": "Constraints are rules on table columns that ensure data integrity. PRIMARY KEY uniquely identifies rows, FOREIGN KEY links tables, NOT NULL prevents empty values, and UNIQUE prevents duplicates.",
                "body_html": """<p>Constraints maintain consistency and reliability of data.</p>
<table>
  <thead><tr><th>Constraint</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>PRIMARY KEY</td><td>Uniquely identifies each record</td></tr>
    <tr><td>FOREIGN KEY</td><td>Establishes relationships between tables</td></tr>
    <tr><td>NOT NULL</td><td>Prevents empty values</td></tr>
    <tr><td>UNIQUE</td><td>Ensures no duplicate values</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Keys in SQL",
                "summary": "Keys identify records and create relationships. A Primary Key uniquely identifies each row and cannot be null. A Foreign Key links one table to another and maintains referential integrity.",
                "body_html": """<table>
  <thead><tr><th>Key Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>Primary Key</td><td>Unique identifier per row, cannot be null or duplicate</td></tr>
    <tr><td>Foreign Key</td><td>Links to a primary key in another table, maintains referential integrity</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "SQL Operations (Conceptual)",
                "summary": "SQL supports retrieving, filtering, sorting, and grouping data. These operations allow users to analyze and manage data effectively without modifying the database structure.",
                "body_html": """<p>SQL supports various operations for working with data:</p>
<ul>
  <li><strong>Retrieving</strong> specific data from tables</li>
  <li><strong>Filtering</strong> data based on conditions</li>
  <li><strong>Sorting</strong> results in ascending or descending order</li>
  <li><strong>Grouping</strong> data for analysis and reporting</li>
</ul>"""
            },
            {
                "heading": "Joins (Conceptual)",
                "summary": "Joins combine data from multiple tables using related columns. Inner Join returns only matching rows. Left and Right Joins include all rows from one side. Full Join returns all rows from both tables.",
                "body_html": """<table>
  <thead><tr><th>Join Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>Inner Join</td><td>Returns matching records from both tables</td></tr>
    <tr><td>Left Join</td><td>All records from left table plus matches from right</td></tr>
    <tr><td>Right Join</td><td>All records from right table plus matches from left</td></tr>
    <tr><td>Full Join</td><td>All records from both tables</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Aggregate Functions and Normalization",
                "summary": "Aggregate functions like COUNT, AVG, and MAX perform calculations on sets of values. Normalization organizes data into related tables to reduce redundancy and improve efficiency.",
                "body_html": """<h3>Aggregate Functions</h3>
<p>Perform calculations on a set of values and return a single result.</p>
<ul>
  <li>Count the number of records</li>
  <li>Find average, maximum, or minimum values</li>
</ul>
<h3>Normalization</h3>
<p>Process of organizing data to reduce redundancy by dividing data into multiple related tables.</p>"""
            },
            {
                "heading": "Advantages, Limitations, and Applications",
                "summary": "SQL is easy to learn, efficient, and widely supported. It is used in banking, e-commerce, and analytics. Its main limitations are less flexibility for unstructured data and requiring a predefined schema.",
                "body_html": """<h3>Advantages</h3>
<ul>
  <li>Easy to learn and use</li>
  <li>Efficient data management for large databases</li>
  <li>Widely supported across platforms</li>
</ul>
<h3>Limitations</h3>
<ul>
  <li>Less flexible for unstructured data</li>
  <li>Requires a predefined schema</li>
</ul>
<h3>Real-World Applications</h3>
<ul>
  <li>Banking systems and e-commerce platforms</li>
  <li>Social media applications</li>
  <li>Data analytics and reporting</li>
</ul>"""
            },
        ],
        "quiz": [
            {"question": "Which SQL command retrieves data from a table?", "options": ["INSERT", "UPDATE", "SELECT", "DELETE"], "answer": 2},
            {"question": "Which join returns all rows from the left table?", "options": ["INNER JOIN", "RIGHT JOIN", "LEFT JOIN", "FULL JOIN"], "answer": 2},
            {"question": "Which constraint uniquely identifies each row?", "options": ["FOREIGN KEY", "UNIQUE", "PRIMARY KEY", "NOT NULL"], "answer": 2},
            {"question": "Which SQL category does the SELECT command belong to?", "options": ["DDL", "DML", "DQL", "DCL"], "answer": 2},
            {"question": "Which aggregate function counts the number of rows?", "options": ["SUM", "AVG", "COUNT", "MAX"], "answer": 2},
        ]
    },
    # Databases Unit 2
    {
        "title": "MongoDB Concepts",
        "unit_number": 2,
        "content": "NoSQL concepts, MongoDB documents and collections, CRUD operations, and advantages of MongoDB for modern applications.",
        "category": "databases",
        "author": "Admin",
        "sections": [
            {
                "heading": "Introduction to NoSQL Concepts",
                "summary": "NoSQL databases handle large volumes of unstructured data without fixed schemas. They offer flexibility, scalability, and high performance for real-time systems, big data, and distributed applications.",
                "body_html": """<p>NoSQL databases are designed to handle large volumes of unstructured or semi-structured data. Unlike traditional relational databases, they do not rely on fixed schemas and tables.</p>
<table>
  <thead><tr><th>Characteristic</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>Schema-less</td><td>No fixed structure required for data</td></tr>
    <tr><td>High Scalability</td><td>Easily scales to handle large datasets</td></tr>
    <tr><td>Flexible Storage</td><td>Supports various data formats</td></tr>
    <tr><td>Performance</td><td>Optimized for large-scale and real-time data</td></tr>
  </tbody>
</table>
<p>MongoDB is one of the most popular NoSQL databases and stores data in a flexible, document-oriented format.</p>"""
            },
            {
                "heading": "Documents and Collections",
                "summary": "MongoDB uses documents (JSON-like data units) and collections (groups of related documents) instead of tables and rows. Documents can have different structures within the same collection.",
                "body_html": """<table>
  <thead><tr><th>Concept</th><th>Description</th><th>SQL Equivalent</th></tr></thead>
  <tbody>
    <tr><td>Document</td><td>Basic unit of data stored in JSON-like format; supports nested and complex data</td><td>Row</td></tr>
    <tr><td>Collection</td><td>Group of related documents; does not enforce a strict schema</td><td>Table</td></tr>
  </tbody>
</table>
<ul>
  <li>Documents can have different structures within the same collection</li>
  <li>Data can be nested and hierarchical</li>
  <li>Flexible structure allows design based on application needs</li>
</ul>"""
            },
            {
                "heading": "CRUD Operations in MongoDB",
                "summary": "CRUD stands for Create, Read, Update, and Delete — the basic operations for interacting with data. These operations form the foundation of database interaction in any application.",
                "body_html": """<table>
  <thead><tr><th>Operation</th><th>Purpose</th></tr></thead>
  <tbody>
    <tr><td>Create</td><td>Adding new data to the database</td></tr>
    <tr><td>Read</td><td>Retrieving data from the database</td></tr>
    <tr><td>Update</td><td>Modifying existing data</td></tr>
    <tr><td>Delete</td><td>Removing data from the database</td></tr>
  </tbody>
</table>
<p>These operations form the foundation of database interaction in any application.</p>"""
            },
            {
                "heading": "Advantages and Conclusion",
                "summary": "MongoDB offers flexible schema design, high performance for large-scale apps, easy integration with modern technologies, and suitability for real-time and distributed systems.",
                "body_html": """<ul>
  <li>Flexible schema design</li>
  <li>High performance for large-scale applications</li>
  <li>Easy integration with modern technologies</li>
  <li>Suitable for real-time and distributed systems</li>
</ul>
<p>MongoDB provides a flexible and scalable approach to data management. Understanding NoSQL concepts, documents, collections, and CRUD operations is essential for working with modern database systems.</p>"""
            },
        ],
        "quiz": [
            {"question": "What type of database is MongoDB?", "options": ["Relational", "NoSQL", "Graph", "Columnar"], "answer": 1},
            {"question": "What is a document in MongoDB?", "options": ["A table of rows", "A basic unit of data stored in JSON-like format", "A database schema", "A type of index"], "answer": 1},
            {"question": "What is a collection in MongoDB equivalent to in SQL?", "options": ["A row", "A column", "A table", "A database"], "answer": 2},
            {"question": "What does CRUD stand for?", "options": ["Create, Run, Update, Delete", "Create, Read, Update, Delete", "Copy, Read, Undo, Delete", "Create, Read, Upload, Drop"], "answer": 1},
            {"question": "Which of the following is a key advantage of MongoDB?", "options": ["Fixed schema design", "Only supports small datasets", "Flexible schema and high scalability", "Requires SQL queries"], "answer": 2},
        ]
    },
    # Databases Unit 3
    {
        "title": "Advanced MongoDB",
        "unit_number": 3,
        "content": "Indexing for performance, aggregation for data analysis, database design principles, and optimization techniques in MongoDB.",
        "category": "databases",
        "author": "Admin",
        "sections": [
            {
                "heading": "Indexing",
                "summary": "Indexing improves data retrieval speed by allowing faster search operations on specific fields. It reduces query time and database load but excessive indexing can increase storage and affect write performance.",
                "body_html": """<p>Indexing is a technique used to improve the speed of data retrieval in a database.</p>
<ul>
  <li>Indexes allow faster search operations</li>
  <li>They reduce the time required to locate data</li>
  <li>Indexes are created on specific fields</li>
  <li>Improves query performance and reduces database load</li>
</ul>
<p>However, excessive indexing can increase storage usage and affect write performance.</p>"""
            },
            {
                "heading": "Aggregation",
                "summary": "Aggregation performs calculations on data to produce summarized results. It combines multiple operations into a single process and is used for reporting, analytics, and generating insights from large datasets.",
                "body_html": """<p>Aggregation is the process of performing calculations on data to produce summarized results.</p>
<ul>
  <li>Used to analyze and transform data</li>
  <li>Combines multiple operations into a single process</li>
  <li>Helps generate insights from large datasets</li>
</ul>
<p>Aggregation is commonly used for reporting, analytics, and data processing.</p>"""
            },
            {
                "heading": "Database Design",
                "summary": "Database design structures data efficiently to meet application requirements. Good design organizes data based on needs, avoids duplication, and ensures efficient access, improving performance and maintainability.",
                "body_html": """<p>Database design refers to structuring data efficiently to meet application requirements.</p>
<ul>
  <li>Organizing data based on application needs</li>
  <li>Choosing appropriate data structures</li>
  <li>Avoiding unnecessary duplication</li>
  <li>Ensuring efficient data access</li>
</ul>
<p>Good database design improves performance, scalability, and maintainability.</p>"""
            },
            {
                "heading": "Optimization",
                "summary": "Optimization improves database operation performance through efficient query design, proper indexing, reducing unnecessary data retrieval, and monitoring. It ensures smooth operation even with large amounts of data.",
                "body_html": """<table>
  <thead><tr><th>Technique</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>Efficient Query Design</td><td>Write queries that retrieve only necessary data</td></tr>
    <tr><td>Proper Indexing</td><td>Use indexes on frequently queried fields</td></tr>
    <tr><td>Reduce Retrieval</td><td>Avoid fetching unnecessary fields or documents</td></tr>
    <tr><td>Performance Monitoring</td><td>Regularly track and tune database performance</td></tr>
  </tbody>
</table>"""
            },
            {
                "heading": "Best Practices and Conclusion",
                "summary": "Design collections based on usage patterns, use indexing wisely, avoid data duplication, optimize queries, and monitor performance regularly. These practices are essential for efficient and high-performing applications.",
                "body_html": """<h3>Best Practices</h3>
<ul>
  <li>Design collections based on application usage patterns</li>
  <li>Use indexing wisely to balance performance</li>
  <li>Avoid unnecessary data duplication</li>
  <li>Optimize queries for better performance</li>
  <li>Regularly monitor database performance</li>
</ul>
<h3>Conclusion</h3>
<p>Advanced MongoDB concepts focus on improving performance and scalability. Indexing, aggregation, and proper database design are essential for building efficient and high-performing applications.</p>"""
            },
        ],
        "quiz": [
            {"question": "What is the purpose of indexing in MongoDB?", "options": ["Store more documents", "Improve data retrieval speed", "Delete duplicate data", "Create collections"], "answer": 1},
            {"question": "What does aggregation do in MongoDB?", "options": ["Deletes old data", "Performs calculations to produce summarized results", "Creates new collections", "Backs up the database"], "answer": 1},
            {"question": "What is a risk of excessive indexing?", "options": ["Faster reads", "Fewer collections", "Increased storage usage and slower writes", "Improved aggregation"], "answer": 2},
            {"question": "What does good database design help achieve?", "options": ["More complex queries", "Performance, scalability, and maintainability", "Larger document sizes", "Fewer CRUD operations"], "answer": 1},
            {"question": "Which technique involves writing queries that retrieve only necessary data?", "options": ["Indexing", "Aggregation", "Efficient Query Design", "Schema Design"], "answer": 2},
        ]
    },
]

def seed():
    db.articles.drop()
    db.units.drop()

    db.articles.insert_many([
        {"title": "Introduction to Hindi", "content": "Hindi is one of the official languages of India, spoken by hundreds of millions of people.", "category": "language", "author": "Admin", "createdAt": datetime.utcnow()},
        {"title": "Common Hindi Phrases",  "content": "Learn everyday Hindi phrases like Namaste (Hello), Dhanyavaad (Thank you), and Kripaya (Please).", "category": "phrases", "author": "Admin", "createdAt": datetime.utcnow()},
    ])

    db.units.insert_many([{**u, "createdAt": datetime.utcnow()} for u in units_data])

    print(f"Seeded {len(units_data)} units across 5 subjects.")

if __name__ == "__main__":
    seed()
