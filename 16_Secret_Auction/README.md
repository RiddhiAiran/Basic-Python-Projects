# Secret Auction Program

Welcome to the **Secret Auction Program**! This interactive application enables users to participate in a simulated auction, determine the highest bidder, and announce the winner in an engaging and user-friendly manner.

---

## Program Demo
Here’s a quick look at how the Secret Auction works:

---

## 🚀 Features

- **Dynamic Bidding System:** Allows multiple users to place their bids secretly.
- **Winner Announcement:** Determines and announces the highest bidder with their bid amount.
- **Clean Interface:** Clears the screen between inputs to maintain privacy.
- **User Prompts:** Guides users with clear and interactive prompts.

---

## 📚 Concepts Used

This program utilizes key Python concepts:

1. **Dictionaries:** Stores bidder names and their respective bids.
2. **Loops and Conditionals:** Handles user input and decision-making.
3. **Functions:** Encapsulates logic for modular and reusable code.
4. **Dynamic Input Handling:** Manages names and bid amounts interactively.

---

## 📄 How to Run the Program

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RiddhiAiran/Basic-Python-Projects.git
   cd 16_Secret_Auction
   ```

2. **Run the Program:**
   Ensure Python is installed on your system. Execute the script using:
   ```bash
   python secret_bid.py
   ```

3. **Follow the Prompts:**
   - Enter the bidder’s name and bid amount.
   - Choose whether to add more bidders.
   - View the winner and their bid once bidding concludes.

---

## Code Explanation

### Main Functions

1. **`highest_bid(bidders)`**:
   - Iterates through the dictionary of bidders and their bids.
   - Determines the highest bid and the corresponding bidder's name.

2. **`auction()`**:
   - Manages the bidding process, collecting bids and handling additional bidders.
   - Utilizes `highest_bid()` to determine the winner and displays the result.

3. **`main()`**:
   - Provides an entry point for the program, allowing users to start or exit the auction.

---

## Example Output

```plaintext
Welcome to the Secret Auction!
What is your name?: Alice
What's Your Bid: $250
Are there any other bidders? Type 'yes' or 'no': yes

What is your name?: Bob
What's Your Bid: $300
Are there any other bidders? Type 'yes' or 'no': no

The winner of this auction is Bob with a bid of $300
```

---

## 🚑 Acknowledgements

This program was created as a fun project to demonstrate the basics of auctions using Python. It’s a beginner-friendly exercise in dictionaries, loops, and interactive applications.

---

Enjoy Coding! 🏆
