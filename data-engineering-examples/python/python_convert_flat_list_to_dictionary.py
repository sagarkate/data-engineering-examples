def get_dict_from_flat_list(flat_list: list) -> dict:
    keys = flat_list[::2]
    values = flat_list[1::2]
    new_dict = dict(zip(keys, values))
    return new_dict

def main():
    my_flat_list = ["id", 1001, "name", "Sagar", "subject", "Maths"]
    print(f"Flat List: {my_flat_list}")
    my_new_dict = get_dict_from_flat_list(my_flat_list)
    print(f"New Dictionary from Flat List: {my_new_dict}")

if __name__ == "__main__":
    main()
