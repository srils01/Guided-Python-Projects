import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
       city=input("Would you like to see data for Chicago, New York, or Washington? Please enter in lowercase").lower()
       if city in CITY_DATA:
            print(CITY_DATA[city])
            file_dataframe=pd.read_csv(CITY_DATA[city])
            break
       else:
            print("Please enter the valid city name")

    while True:
        filter=input("Would you like to filter the data by month, day, or not at all?").lower()
        if filter!="month" and filter!="day":
            prompt=input("Would you like to see the raw data?").lower()
            if prompt=="yes":
                start=0
                end=4
                while True:
                    print(file_dataframe.loc[start:end])
                    end+=5
                    prompt=input("Do you wish to continue?: ").lower()
                    if prompt!="yes":
                        break
        if filter == "day":
            day=input("which day?Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday ? Please enter in lowercase").lower()
            if day in DAY_DATA:
                month=input("Which month? january, February, March, April,May or June ? Please enter in lowercase").lower()
                if month in MONTH_DATA:
                    return city, month,day
        if filter == "month":
            month=input("Which month? january, February, March, April,May or June ? Please enter in lowercase").lower()
            if month in MONTH_DATA:
                day=input("which day?Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday ? Please enter in lowercase").lower()
            if day in DAY_DATA:
                return city, month,day
    print('-'*40)


def load_data(city, month, day):
    print("Loading data as per the user input")
    print(CITY_DATA[city])
    dataframe_data=pd.read_csv(CITY_DATA[city])
    return dataframe_data


def time_stats(dataframe_data):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    start_time_dataframe= dataframe_data["Start Time"]
    date_dataframe = pd.to_datetime(start_time_dataframe)
    month_dataframe = date_dataframe.dt.month
    most_common_month= month_dataframe.mode()[0]
    print("The most common month is", (most_common_month))
    day_dataframe = date_dataframe.dt.weekday
    most_common_day=day_dataframe.mode()[0]
    print("The most common day is",(most_common_day))
    hour_dataframe=date_dataframe.dt.hour
    most_common_hour=hour_dataframe.mode()[0]
    print("The most common hour is",(hour_dataframe))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(dataframe_data):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    start_station_dataframe= dataframe_data["Start Station"]
    most_popular_start_station=start_station_dataframe.mode()[0]
    print("The most popular start station is",(most_popular_start_station))
    end_station_dataframe= dataframe_data["End Station"]
    most_popular_end_station=end_station_dataframe.mode()[0]
    print("The most popular end station is",(most_popular_end_station))
    combination=start_station_dataframe+end_station_dataframe
    most_common_combination=combination.mode()[0]
    print("The most popular combination of stations is",(most_common_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(dataframe_data):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    travel_time_dateframe=dataframe_data["Trip Duration"].sum()
    print("The total travel time is ", travel_time_dateframe)
    mean_travel_time_dateframe=dataframe_data["Trip Duration"].mean()
    print("The mean travel time is ",mean_travel_time_dateframe)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(dataframe_data):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_type_dataframe=dataframe_data["User Type"]
    count_user_type=user_type_dataframe.value_counts()
    print("The count of user types is", (count_user_type))
    if "Gender" in dataframe_data:
        gender_dataframe=dataframe_data["Gender"]
        count_of_gender=gender_dataframe.value_counts()
        print("The count of gender is", (count_of_gender))
    else:
        print("Gender stats cannot be calculated because Gender does not appear in the dataframe")
    if "Birth Year" in dataframe_data:
        year_dataframe=dataframe_data["Birth Year"]
        earliest_year=year_dataframe.min()
        print("The earliest year of birth is", (earliest_year))
        most_recent_year=year_dataframe.max()
        print("The most recent year of birth is", (most_recent_year))
        most_common_year=year_dataframe.mode()[0]
        print("The most common year of birth is", (most_common_year))
    else:
        print("Birth year stats cannot be calculated because birth year does not appear in the dataframe")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        print("City value returned is --- ",city)
        print("Month value returned is --- ",month)
        print("Day value returned is --- ",day)
        dataframe_data= load_data(city, month, day)
        time_stats(dataframe_data)
        station_stats(dataframe_data)
        trip_duration_stats(dataframe_data)
        user_stats(dataframe_data)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
