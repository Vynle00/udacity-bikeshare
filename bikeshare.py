import time
import pandas as pd
import numpy as np

CITY_DATA = { 'CHICAGO': 'chicago.csv',
              'NEW YORK CITY': 'new_york_city.csv',
              'WASHINGTON': 'washington.csv' }


# this comment serves as a refactoring #1

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #make variable for all the cities that are acceptable
    cities = ['CHICAGO', 'NEW YORK CITY', 'WASHINGTON']
    #go through a while loop to see if that value is present in the list
    while True:
        city = input("Enter one of the folliwng cities (Chicago, New York City, Washington:").upper()
        if city in cities:
            print('will use ', city , ' as the city....')
            break
        else:
            print('Please enter a city from the list')

    # TO DO: get user input for month (all, january, february, ... , june)
    #make variable for all the months that are acceptable
    months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'ALL']
    #go through a while loop to see if that value is present in the list
    while True:
        month = input("Enter one of the folliwng months (January, February, March, April, May, June) or enter all:").upper()
        if month in months:
            print('will use ', month , ' as the month....')
            break
        else:
            print('Please enter a month from the list')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #make variable for all the days that are acceptable
    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY','ALL']
    #go through a while loop to see if that value is present in the list
    while True:
        day = input("Enter one of the folliwng day of the week (Monday, Tuesday, Wednesday, Thursday, Friday) or enter all:").upper()
        if day in days:
            print('will use ', day , ' as the day....')
            break
        else:
            print('Please enter a day from the list')    
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'ALL':
        # use the index of the months list to get the corresponding int
        months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'ALL':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    month_dict = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June'
    }
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an month     column
    df['month'] = df['Start Time'].dt.month

    # find the most popular month
    popular_month = df['month'].mode()[0]
    
    #print and convert number to month
    print('Most Popular Month: ' + month_dict.get(popular_month))

    # TO DO: display the most common day of week
    # find the most popular day
    popular_day = df['day_of_week'].mode()[0]
    
    print('Most Popular day of week: ' + popular_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

# find the most popular hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    
    print('Most popular start station: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    
    print('Most popular end station: ' , popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_and_end_station = df[['Start Station','End Station']].mode().loc[0]
    
    print('Most Common combination of start station and end station: ' , popular_start_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total time that was traveled: ', total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean traveled time: ', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    
    print('User Type count: ', user_type_count)

    # TO DO: Display counts of gender
    #need to see if it is city that has the information if not need to handle exception
    try:
        user_gender_count = df['Gender'].value_counts()
    
        print('Gender count: ', user_gender_count)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
    
        print('Earliert Birth Year: ', earliest_birth_year)
          
        recent_birth_year = df['Birth Year'].max()
    
        print('Recent Birth Year: ', recent_birth_year)
    
        common_birth_year = df['Birth Year'].mode()
    
        print('Common Birth Year: ', common_birth_year)
    except:
        print('This city does not have gender and birth year information')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    #Getting the raw data in 5 rows at a time
def raw_data(df):
    #init variables to use in while loop
    start_index = 0
    max_count = len(df.index)
    
    while start_index < max_count:
        #asking user if they would like to see the data in increments of 5s
        view_raw_data = input('Would you like to see the raw data in increments of 5 ? (yes/no): ').upper()
        if view_raw_data == 'YES':
            #getting the the next 5 rows and printing it out 
            print('printing the data next 5 rows of data: ', df.iloc[start_index:(start_index +5)])
            #iterating the varible by 5 to keep track of what has already been printed
            start_index += 5
        else:
            break
    
# this comment serves as a refactoring #2

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').upper()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
