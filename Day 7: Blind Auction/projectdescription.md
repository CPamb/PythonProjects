# Auction Bidding System

Welcome to the Auction Bidding System! This Python script allows users to participate in an auction by submitting their bids and determining the highest bidder.

## How it Works

1. **Initialization:**
   - The program starts by displaying the logo using ASCII art and initializing an empty dictionary to store bids.

2. **Bidding Process:**
   - Users are prompted to enter their name and the bid amount.
   - The bid information is stored in a dictionary with the bidder's name as the key and the bid amount as the value.

3. **End of Bidding:**
   - Users are asked if there are any other bidders.
   - If there are no more bidders, the program determines the highest bidder and announces the winner.
   - If there are more bidders, the process continues.

4. **Determining the Winner:**
   - The program iterates through the bid records to find the highest bid and the corresponding bidder.
   - Once the highest bidder is determined, the program announces the winner.
