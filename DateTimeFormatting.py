# '''Datetime formatting example'''
# import datetime
# my_date = datetime.datetime(2018,12,29,10,30,45)
# print(my_date)
#
# ##print date in 'Month <date>, year' format. Ex December 29, 2017
# frmt_date = '{:%B %d, %Y}'.format(my_date)
# print(frmt_date)
#
# # print date as 'December 07, 2017 fell on <day of the week> and was <day> of the year
# frmt_date = '{0:%B %d, %Y} fall on a {0:%A} and will be the {0:%j} of the year.'.format(my_date)
# print(frmt_date)

import calendar
year = int(input('enter a year:'))
if calendar.isleap(year) == True:
    print(str(year) + ' ' + 'is leap year')
else:
    print(str(year) + ' ' + 'is not leap year')
