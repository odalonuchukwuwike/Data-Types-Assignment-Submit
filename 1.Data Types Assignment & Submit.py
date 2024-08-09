capital = 1000;
daily_increase = 0.12;
i = 1;
period = 7;
#growth_rate = 1;
while (i <= period):
  capital = capital + (capital * daily_increase);
  i = i  + 1;
final_growth_rate = capital;
final_growth_rate = round(final_growth_rate, 2);
print("Your money is ${}".format(final_growth_rate));