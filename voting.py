#!/usr/bin/env python3

#Application for a user to make ballot selections for awards program

ballot = []
awards = [
    ["Outstanding Drama Series", [
        "The Diplomat",
        "The Gilded Age",
        "A Knight of the Seven Kingdoms",
        "Paradise",
        "The Pitt",
        "Pluribus",
        "Slow Horses",
        "Your Friends & Neighbors"
    ]],
    ["Outstanding Comedy Series", [
        "Abbott Elementary",
        "The Bear",
        "Hacks",
        "Margo's Got Money Troubles",
        "Nobody Wants This",
        "Only Murders in the Building",
        "Shrinking",
        "Widow's Bay"
    ]],
    ["Outstanding Lead Actress In A Comedy Series", [
        "Quinta Brunson, Abbot Elementary",
        "Ayo Edebiri, The Bear",
        "Elle Fanning, Margo's Got Money Troubles",
        "Lisa Kudrow, The Comeback",
        "Jean Smart, Hacks"
    ]],
    ["Outstanding Lead Actor In A Comedy Series", [
        "Yahya Abdul-Mateen II, Wonder Man",
        "Steve Carell, Rooster",
        "Matthew Rhys, Widow's Bay",
        "Jason Segel, Shrinking",
        "Martin Short, Only Murders in the Building"
    ]],
    ["Oustanding Guest Actress in a Comedy Series", [
        "Leslie Bibb, Hacks",
        "Jamie Lee Curtis, The Bear",
        "Betty Gilpin, Widow's Bay",
        "Cherry Jones, Hacks",
        "Laurie Metcalf, Hacks",
        "Kaitlin Olson, Hacks",
        "Lauren Weedman, Hacks"
    ]],
    ["Outstanding Variety Series", [
        "The Daily Show",
        "Jimmy Kimmel Live!",
        "Last Week Tonight with John Oliver",
        "The Late Show with Stephen Colbert",
        "Saturday Night Live"
    ]],
    ["Outstanding Writing for a Variety Series", [
        "Jimmy Kimmel Live!",
        "Last Week Tonight with John Oliver",
        "The Late Show with Stephen Colbert"
    ]],
    ["Outstanding Reality Competition Program", [
        "Dancing with the Stars",
        "RuPaul's Drag Race",
        "Survivor 50",
        "Top Chef",
        "The Traitors"
    ]]]

def main():
    print("Welcome to the 78th Primetime Emmy Awards")
    for category, nominees in awards:
        ballot.append([category, selection(category, nominees)])
    ballot_display(ballot)

def selection(category, nominees):
    print("=" * 78)
    print(f"The nominees for {category} are:\n")
    print(f"[1] Write-in")
    for index, val in enumerate(nominees, start=2):
        print(f"[{index}] {val}")

    while True:
        choice = int(input(f"Please enter your choice for {category} now: " ))
        if choice == 1:
            result = input(f"Please enter your write-in candidate: ")
            break
        elif 2 <= choice <= (len(nominees) + 1):
            result = nominees[choice - 2]
            break
        else:
            print(f"I'm sorry, but {choice} is not a valid option.")
    print(f"Thank you for selecting {result} as {category}")
    return result

def ballot_display(ballot):
    print(f"Thank you for voting. Here is a summary of your votes: ")
    for category, choice in ballot:
        print(f"{category} :\n\t{choice}\n")

if __name__ == "__main__":
    main()