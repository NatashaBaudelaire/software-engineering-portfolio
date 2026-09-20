# Database Design and Modeling

Exercises on relational database design across the three abstraction levels of
database modeling: conceptual, logical and physical. Each exercise follows the
full path from an Entity-Relationship diagram to an executable SQL schema.

## Directory Structure

### `conceptual-model`

High-level Entity-Relationship (ER) diagrams with entities, relationships and
business rules, without implementation details.

| File | Domain |
| --- | --- |
| `cleaning.png` | Cleaning service company |
| `order.png` | Orders and customers |
| `pharmacy.png` | Pharmacy sales |
| `physical-activity.png` | Physical activity tracking |

### `logical-model`

Relational schemas derived from the conceptual models: tables, attributes,
keys and relationships, including normalization decisions.

| File | Domain |
| --- | --- |
| `cars.png` | Car rental |
| `company.png` | Company departments and employees |
| `pharmacy.png` | Pharmacy sales |
| `salesperson.png` | Salesperson management |
| `seller.png` | Seller management |
| `traffic.png` | Traffic infractions |
| `vehicle.png` | Vehicle registry |

### `physical-model`

Implementation-ready SQL DDL scripts with constraints, primary/foreign keys
and sample DML data.

| File | Domain |
| --- | --- |
| `car.sql` | Car rental |
| `company.sql` | Company departments and employees |
| `infraction.sql` | Traffic infractions |
| `pharmacy.sql` | Pharmacy sales |
| `register.sql` | Sales register |
| `salesperson.sql` | Salesperson management |
| `seller.sql` | Seller management |
| `traffic.sql` | Traffic infractions |
| `vehicle.sql` | Vehicle registry |

## How to Use

1. Review the conceptual diagram for the domain.
2. Compare it with the logical model (normalization, keys, cardinality).
3. Execute the physical model script in a relational database:

```sql
mysql -u username -p database_name < pharmacy.sql
```

## Learning Objectives

- Entity-Relationship modeling and cardinalities
- Mapping ER models to relational schemas
- Normalization (1NF, 2NF, 3NF)
- Primary and foreign keys, check constraints and referential integrity
- SQL DDL and DML: `CREATE TABLE`, `INSERT`, constraints