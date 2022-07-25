"""DropDrop"""
def main():
    """DropDrop"""
    grade = float(input())
    if grade < 1.00:
        print("I'm so sad.")
    elif grade < 2.00:
        wgrade = 4.00-grade
        print("%.2f"%wgrade)
    elif grade >= 2.00:
        print("I'm so happy.")
main()
