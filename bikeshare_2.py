import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    correct_cities = ['chicago', 'new york','washington']
    while city not in correct_cities:
        city = input("Would you like 'chicago', 'new york' or 'washington': ").lower()
        if city in correct_cities:
            break
        else:
            print("Please enter a correct city. 'chicago', 'new york' or 'washington'.")

    # get user input for month (all, january, february, ... , june)
    month = ""
    correct_months = ['january', 'february','march','april','may','june','all']
    while month not in correct_months:
        month = input("Would you like 'all' or a month ('January'-'June')?").lower()
        if month in correct_months:
            break
        else:
            print("Please enter a correct month.")
            print("'january', 'february','march','april','may','june'")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    correct_days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while day not in correct_days:
        day = input("Please enter 'all' or select a day ('monday' - 'sunday'): ").lower()
        if day in correct_days:
            break
        else:
            print("Please enter a correct day.")
            print("'monday','tuesday','wednesday','thursday','friday','saturday','sunday'")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    
    df = pd.read_csv('Final Project\\' + CITY_DATA[city.lower()])
    

    df['Start Time'] = pd.to_datetime(df["Start Time"])

    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':    
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    print(df)


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print(common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(common_day)


    # display the most common start hour
    common_hour = df['Start Time'].dt.hour
    print(common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(common_end_station)


    # display most frequent combination of start station and end station trip
    common_both_station = (df['Start Station'] + df['End Station']).mode()[0]
    print(common_both_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""


    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print(user_type_count)


    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    except:
        print("There is no 'Gender' column for that dataframe")


    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print(earliest_birth_year)   
        most_recent_birth_year = df['Birth Year'].max()
        print(most_recent_birth_year)   
        most_common_birth_year = df['Birth Year'].mode()[0]
        print(most_common_birth_year)   
    except:
        print("There is no 'Birth Year' column for that dataframe.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_raw_data(df):
    view_raw = ""
    correct_answers = ['yes', 'no']
    while view_raw not in correct_answers:
        view_raw = input("Would you like to view raw data 5 lines at a time?: ").lower()
        print(view_raw)

    data_iter = 0
    while view_raw == 'yes':
        print(df[data_iter:data_iter+5])
        view_raw = input("Would you like to view the next 5 rows of data?: ").lower()
        if view_raw == "no" or data_iter > len(df):
            break
        elif view_raw == "yes":
            data_iter += 5



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        view_raw_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
