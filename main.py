from fractions import Fraction
from rich import print
from Proxima.usr_inputs import UI_Inputs

ui = UI_Inputs()


def main():

    # Asks the user how many points they have
    print('\nHow many [bold blue]points[/] do you have?')
    num_points = ui.ask_for(': ', '\nNot an integer', int)

    # Find points and store them in a list
    def find_points():
        print(
            '\nPlease input the value below | ( EX: 3, hit enter, then 7) \nThis will also loop over for however many points you have.')
        point = float(input('\nPoint 1: '))
        point2 = float(input('\nPoint 2: '))
        point_list = []
        point_list.append(point)
        point_list.append(point2)
        not_point = False
        return point_list

    print(
        '\nWhat [bold blue]operation[/] would you like to perform to each point?')
    print(
        'M = [bold blue]Multiply[/]')
    operation = ui.ask_for('\n: ', 'Not a string', str).upper()

    # * Multiplication
    if operation == 'M':

        # * Scale factor and fraction
        print(
            "\nWhat is the [bold blue]scale factor[/]? ( The number you're multiplying everything by )")
        print('\nIs the scale factor a fraction? (y/n)')
        not_fraction = ui.ask_for('\n: ', 'Not an answer.', str).lower()

        # * User is using a fraction
        if not_fraction == 'y':
            print('\nWhat is the fraction?')
            scale_factor_fraction = ui.ask_for('\n:')
            fraction_factor = Fraction(scale_factor_fraction)
            # * Do math stuff here
            for _ in range(num_points):
                points = find_points()

                #! Math stuff here ( list comprehension )
                new_points = [element * fraction_factor for element in points]
                print(new_points)

        # * User is not using a fraction
        if not_fraction == 'n':
            print('\nScale factor ( integer or decimal )')
            scale_factor = input('\n: ')
            scale_factor = float(scale_factor)
            # * Do math stuff here

            for _ in range(num_points):
                points = find_points()

                #! Math stuff here ( list comprehension )
                new_points = [element * scale_factor for element in points]
                print(new_points)


if __name__ == "__main__":
    main()
