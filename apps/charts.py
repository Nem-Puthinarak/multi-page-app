import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def draw_charts(df):
    st.title('Data Graph')

    st.write("This is the `Data Graph` page of the multi-page app.")

    st.write("Here are histograms for each feature based on the data from the `Data` page.")

    # Ensure 'class' column is treated as categorical
    df['class'] = df['class'].astype('category')

    # Select only the features (excluding the 'class' column)
    features = df.drop(columns=['class'])

    # Plot histograms for each feature
    for feature in features.columns:
        fig, ax = plt.subplots()
        sns.histplot(data=df, x=feature, kde=True, ax=ax)
        plt.xlabel(feature)
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {feature}')
        st.pyplot(fig)




