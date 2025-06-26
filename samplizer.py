import pandas

orignal_df = pandas.read_csv('dataset.csv')

sample_df = orignal_df.sample(n=1000, random_state=42)

sample_df.to_csv('sample_data.csv', index = False)

