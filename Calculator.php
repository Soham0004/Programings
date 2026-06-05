<!DOCTYPE html>
<html>
    <head>
        <title>Simple Calculator</title>
    </head>
    <body>
        <h2>Simple Calculator</h2>
        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            <input type="text" name="num1" placeholder="Enter first number" required>
            <select name="operator">
                <option value="add">Addition (+)</option>
                <option value="subtract">Subtraction (-)</option>
                <option value="multiply">Multiplication (*)</option>
                <option value="divide">Division (/)</option>
            </select>
            <input type="text" name="num2" placeholder="Enter second number" required>
            <input type="submit" name="calculate" value="Calculate">
        </form>

        <?php
        // Function to perform calculations
        function calculate($num1, $operator, $num2) {
            switch ($operator) {
                case 'add':
                    return $num1 + $num2;
                    break;
                case 'subtract':
                    return $num1 - $num2;
                    break;
                case 'multiply':
                    return $num1 * $num2;
                    break;
                case 'divide':
                    if ($num2 != 0) {
                        return $num1 / $num2;
                    } else {
                        return "Cannot divide by zero!";
                    }
                    break;
                default:
                    return "Invalid operator";
                    break;
            }
        }

        // Check if the form is submitted
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $num1 = $_POST['num1'];
            $num2 = $_POST['num2'];
            $operator = $_POST['operator'];

            // Validate numeric input
            if (is_numeric($num1) && is_numeric($num2)) {
                $result = calculate($num1, $operator, $num2);
                echo "Result: $num1 $operator $num2 = $result";
            } else {
                echo "Please enter valid numeric values";
            }
        }
        ?>
    </body>
</html>
