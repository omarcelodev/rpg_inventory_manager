# RPG Adventure Inventory Manager

A terminal-based inventory management system for a text RPG, built in Python, allowing players to manage items with categories, quantities, and persistent storage.

## 📜 Description

This project simulates an RPG inventory system where each item has a **name**, **type**, and **quantity**.  
The system prevents duplicate items, validates user input, and saves inventory data between executions using JSON.

It was developed as a final challenge to practice core Python concepts such as data structures, functions, control flow, file handling, and modular logic.

## ⚙️ Features

- Add items to the inventory with quantity selection
- Automatically categorizes items based on predefined game data
- Prevents duplicate items (adds quantity instead)
- Remove items partially or completely
- Validate user input (no zero or negative quantities)
- Inventory capacity limit per item
- View available game items by category
- Display a full inventory summary
- Persistent storage using JSON (save & load inventory)
- Interactive terminal menu

## 🧱 Inventory Rules

- Items are uniquely identified by name
- Each item belongs to a predefined category
- Maximum quantity per item is limited
- Removing more items than available deletes the item from inventory

## 🗂️ Project Structure

- `itens`: predefined game items grouped by category
- `inventario`: dynamic player inventory stored as a list of dictionaries
- Modular functions for each inventory operation
- JSON file used to persist inventory data between runs

## ▶️ How to Run

1. Make sure you have **Python 3.x** installed
2. Clone the repository
3. Run the main file:

```bash
python main.py
```
The inventory will automatically load from inventario.json if it exists.

## 💾 Technologies Used

- Python 3

- Standard libraries:
  - json
  - os

## 🚀 Possible Improvements

- Search inventory by item name

- Edit item quantities directly

- Add item descriptions and rarity levels

- Unit tests

- Refactor input handling with exception control

- Convert to OOP structure

## 📌 Author

Developed by **Marcelo** as a Python learning challenge and portfolio project.
