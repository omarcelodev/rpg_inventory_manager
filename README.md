# RPG Inventory Manager

A terminal-based inventory management system for a text RPG, built with Python. It allows players to manage items, quantities, and categories with persistent storage using JSON.

This project was developed as a learning challenge to practice core Python concepts such as data structures, functions, control flow, input validation, file handling, and modular programming.

## Features

* Add items with a specified quantity
* Automatically categorize items based on predefined game data
* Increase the quantity when an item already exists in the inventory
* Remove items partially or completely
* Validate quantities and user input
* Enforce a maximum quantity per item
* Browse available game items by category
* Display a complete inventory summary
* Save and load inventory data using JSON
* Interactive terminal menu

## Inventory Rules

* Items are uniquely identified by name.
* Each item belongs to a predefined category.
* Each item has a maximum allowed quantity.
* Adding an existing item increases its current quantity.
* Removing the entire available quantity deletes the item from the inventory.
* Invalid quantities, such as zero or negative values, are rejected.

## Project Structure

The application is organized around:

* `itens` — predefined game items grouped by category;
* `inventario` — the player's current inventory, represented as a list of dictionaries;
* dedicated functions for inventory operations;
* `inventario.json` — persistent inventory data created and loaded between executions.

## Technologies

* Python 3
* Python standard library:

  * `json`
  * `os`

No external dependencies are required.

## Getting Started

### Prerequisites

* Python 3.x

### Installation

Clone the repository:

```bash
git clone https://github.com/omarcelodev/rpg-inventory-manager.git
cd rpg-inventory-manager
```

### Running the Application

```bash
python main.py
```

If `inventario.json` already exists, the application automatically loads the previously saved inventory.

## Possible Improvements

* [ ] Search inventory by item name
* [ ] Edit item quantities directly
* [ ] Add item descriptions and rarity levels
* [ ] Add automated tests
* [ ] Improve input validation and exception handling
* [ ] Refactor the application using object-oriented programming

## What I Learned

This project was created to practice fundamental Python concepts through a small but complete terminal application, including:

* data structures;
* functions and control flow;
* input validation;
* JSON serialization and persistence;
* file handling;
* separation of application logic into reusable functions.

## License

This project is licensed under the [MIT License](LICENSE).

© 2025 Marcelo Gomes
