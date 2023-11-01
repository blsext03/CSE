if __name__ == '__main__':
    
    import json
    
    def readfile(animals):
        try:
            with open('animals.json','r') as file:
                animals_data = json.load(file)
            return animals_data
        except FileNotFoundError:
            return []
    
    def menu():
        print("0 - Print all dogs")
        print("1 - Search")
        print("2 - Quit")
        
        
    def printing(animals):
        for animal in animals:
            if animal.get('species') == 'dog':
                print(f""""Name: {animal['name']}, 
                      Breed: {animal['breed']}, 
                      Height: {animal['height']}, 
                      Weight: {animal['weight']}""")

    def search_by_name(animals, name):
        name = input("Would you like to search by name or by breed? ")
        found = False
        for animal in animals:
            if animal['name'] == name:
                print(f""""Name: {animal['name']}, 
                      Breed: {animal['breed']}, 
                      Height: {animal['height']}, 
                      Weight: {animal['weight']}""")
                found = True
            if not found:
                print(f"No animals with the name '{name}' found.")

    def search_by_breed(animals, breed):
        found = False
        for animal in animals:
            if animal['breed'] == breed:
                print(f""""Name: {animal['name']}, 
                      Breed: {animal['breed']}, 
                      Height: {animal['height']}, 
                      Weight: {animal['weight']}""")
                found = True
            if not found:
                print(f"No animals with the breed '{breed}' found.")

    def main():
        file_name = 'animals.json'
        animals = readfile(file_name)
    
        while True:
            menu()
            choice = input("Enter what you would like to do: ")
        
            if choice == '0':
                printing(animals)
            elif choice == '1':
                search_option = input("Would you like to search by name or by breed? ").lower()
                if search_option == 'name':
                    name = input("Enter the name you would like to search: ")
                    search_by_name(animals, name)
                elif search_option == 'breed':
                    breed = input("Enter the breed you would like to search: ")
                    search_by_breed(animals, breed)
                else:
                    print("Invalid search option. Please enter 'name' or 'breed'.")
            elif choice == '2':
                break
            else:
                print("Invalid choice. Please select a valid option.")
