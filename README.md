# Basic Project In Python

## Data Types In Python

- Mutable Data Types
    ```
    list, dict
    ```
- Immutable Data Types
    ```
    str, tuple, int, float
    ```

    

```
🔥 Mini Project 2: Bank System
```

### Base Class: BankAccount

- Attributes: 

```account_number, balance```

- Methods:

```
deposit(amount)

withdraw(amount)

get_balance()
```

## Child Classes:

```SavingsAccount```

```
Extra attribute: interest_rate

Method: add_interest()
```

```CurrentAccount```

```
Extra attribute: overdraft_limit

Override withdraw() to allow overdraft
```

# Challenge:

Prevent withdrawing more than allowed

Show transaction messages