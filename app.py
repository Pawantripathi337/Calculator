from flask import Flask, request

app = Flask(__name__)

def calculate_expression(expression):
    try:
        result = eval(expression)  # Evaluate the mathematical expression
        return result
    except ZeroDivisionError:
        return "Error! Division by zero."
    except Exception:
        return "Invalid expression."

@app.route("/", methods=["GET", "POST"])
def calculator():
    expression = request.form.get("expression", "")
    result = ""

    if request.method == "POST":
        # Check if user pressed the '=' button
        if "calculate" in request.form:
            result = calculate_expression(expression)
        # Check if user pressed the 'Clear' button
        elif "clear" in request.form:
            expression = ""
        # Append the pressed button value to the expression
        else:
            for key in request.form:
                if key not in ["expression", "calculate", "clear"]:
                    expression += key

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python Calculator</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f3f3f3;
                margin: 0;
            }}
            .calculator {{
                background-color: #ffffff;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                max-width: 300px;
                width: 100%;
            }}
            .calculator input[type="text"] {{
                width: 100%;
                height: 50px;
                margin-bottom: 10px;
                font-size: 1.5em;
                padding: 5px;
                text-align: right;
                border: 2px solid #ccc;
                border-radius: 8px;
            }}
            .grid {{
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 10px;
            }}
            .button {{
                padding: 20px;
                font-size: 1.2em;
                text-align: center;
                cursor: pointer;
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 8px;
            }}
            .button.operator {{
                background-color: #007bff;
            }}
            .button.clear {{
                background-color: #dc3545;
                grid-column: span 2;
            }}
            .button:hover {{
                filter: brightness(90%);
            }}
        </style>
    </head>
    <body>
        <form class="calculator" method="post">
            <input type="text" name="expression" value="{expression}" readonly>
            <div class="grid">
                <button type="submit" name="7" class="button">7</button>
                <button type="submit" name="8" class="button">8</button>
                <button type="submit" name="9" class="button">9</button>
                <button type="submit" name="/" class="button operator">÷</button>

                <button type="submit" name="4" class="button">4</button>
                <button type="submit" name="5" class="button">5</button>
                <button type="submit" name="6" class="button">6</button>
                <button type="submit" name="*" class="button operator">×</button>

                <button type="submit" name="1" class="button">1</button>
                <button type="submit" name="2" class="button">2</button>
                <button type="submit" name="3" class="button">3</button>
                <button type="submit" name="-" class="button operator">−</button>

                <button type="submit" name="0" class="button">0</button>
                <button type="submit" name="." class="button">.</button>
                <button type="submit" name="calculate" class="button operator">=</button>
                <button type="submit" name="+" class="button operator">+</button>

                <button type="submit" name="clear" class="button clear">Clear</button>
            </div>

            <div style="margin-top: 20px; font-size: 1.2em; color: #333;">
                <strong>Result: {result}</strong>
            </div>
        </form>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)

