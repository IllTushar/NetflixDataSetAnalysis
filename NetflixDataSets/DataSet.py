from csv_files import CSV_Data as csv


class Data:
    @staticmethod
    def analysis_data():
        list = []
        movie_count = 0
        tv_show_count = 0

        csv_file = csv.csv_data_file()
        type_col = csv_file['type']
        for types in type_col:
            list.append(types)
            if types == 'Movie':
                movie_count = movie_count + 1
            else:
                tv_show_count = tv_show_count + 1

        types_present = set()
        for items in list:
            types_present.add(items)

        print(f"Present things: {types_present}")
        print(f"Movies: {movie_count}")
        print(f"TV_Shows: {tv_show_count}")

    @staticmethod
    def find_country():
        country_lists = []
        csv_file = csv.csv_data_file()
        country_list = csv_file['country']
        for number_of_country in country_list:
            country_lists.append(number_of_country)

        find_specific_country = []
        total_country = set()
        for items in country_list:
            if items == 'India':
                total_country.add(items)
                find_specific_country.append(items)
        print(f"Name of countries: {total_country} \nsize {len(find_specific_country)}")

        india_movie_list = []
        us_movie_list = []
        movie_name = csv_file['title']
        char_of_india_movie = 'I'
        char_of_us = 'Z'
        for i, movies_items in enumerate(movie_name):
            if country_list[i] == 'India' and movies_items.startswith(char_of_india_movie):
                india_movie_list.append(movies_items)
            elif country_list[i] == 'United States' and movies_items.startswith(char_of_us):
                us_movie_list.append(movies_items)

        print(f'Movies name released with character {char_of_india_movie} in India: {india_movie_list}')
        print(f'List size: {len(india_movie_list)}')
        print(f'Movies name released with character {char_of_us} in United States: {us_movie_list}')
        print(f'List size: {len(us_movie_list)}')
