# Follow me on twitter (Nadeem__dev)
name = str(input("Enter Your Name: "))
print(f'''{"*"*38} 
\tMr./Ms. {name} Welcome to KBC
{"*"*38}
NOTE: Write answers first letter in capital''')
question = ["Who had discovered the boolean algebra: ", "What is the summer capital of Kashmir🏳️: ",
            "Who is world's richest person: ", "What is the capital of India: ", "Name the first programmable analog computer: ", "Name the National fruit of India: "]
answers = ["George boole", "Srinagar",
           "Elon musk", "", "Castle clock", "Mango"]


amout = 0
for x in range(len(question)):
    quest = str(input(question[x]))
    if quest == answers[x]:
        amout += 50
        print(f"Correct! {name} You Won : {amout}k ")
    else:
        print(
            f"Wrong, Better luck next time \t You Won Total Amout Of : {amout}k")
        break
