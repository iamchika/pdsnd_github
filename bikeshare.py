import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    while True:
        city= input("\ninput either chicago, new york city, washington\n").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('\ninvalid input. Input either chicago, new york city, washington\n')
    # get user input for month (all, january, february, ... , june)
    while True:
        month= input('Input any of the first six months of the year or "all"\n').lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print('\ninvalid input. Input any of the first six months of the year or "all"\n')
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input("input any day of the week or all\n").lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print('\ninvalid input. Input any day of the week or all\n')

    
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
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month name']= df['Start Time'].dt.month_name()
    print('Most common month is :', df['month name'].mode()[0])


    # display the most common day of week
    print('Most common day of the week is :', df['day_of_week'].mode()[0])
    
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used Start Station is :', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('\nMost commonly used End Station is :', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print('\nMost frequent combination of start station and end station trip is :', df.groupby(['Start Station','End Station']).size().nlargest(1).index[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The total travel time in seconds is:', df['Trip Duration'].sum())

    # display mean travel time
    print('\nThe mean travel time in seconds is:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types are:', df['User Type'].value_counts())
    # Washington does not have gender and birth year columns,
    # So an if statement will help to avoid an error
    if 'Gender' in df:
        # Display counts of gender
        print('\nCounts of gender:', df['Gender'].value_counts())
    if 'Birth Year' in df:
        # Display earliest, most recent, and most common year of birth
        print('\nEarliest year of birth:', df['Birth Year'].min())
        print('\nMost recent year of birth:', df['Birth Year'].max())
        print('\nMost common year of birth:', df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def raw_data(df):
    '''
    Displays raw data based on user\'s input.
    
    Arg:
    df - Pandas DataFrame containing city data filtered by month and day
    '''
    x = 1
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

