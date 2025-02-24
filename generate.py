def int_to_dotmap(n, bits=12):
    """Convert an integer to a dot map with 12-bit representation."""
    binary = f"{n:012b}"  # Convert number to 12-bit binary string
    dots = ["●" if bit == "1" else "○" for bit in binary]
    return " | ".join(["".join(dots[i:i+4]) for i in range(0, 12, 4)])


def generate_dotmap(file_path):
    """Read words from a file and generate a dot map table."""
    with open(file_path, "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]
    
    print("| Index | Word     | Column1 | Column2 | Column3 |")
    print("|-------|----------|---------|---------|---------|")
    
    for idx, word in enumerate(words, start=1):
        dotmap = int_to_dotmap(idx)
        column1, column2, column3 = dotmap.split(" | ")
        print(f"| {idx:<5} | {word:<8} | {column1:<7} | {column2:<7} | {column3:<7} |")


if __name__ == "__main__":
    file_path = "wordlist.txt"  
    generate_dotmap(file_path)

