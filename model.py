
model = joblib.load('model.pkl')
st.title = "Spam detection model"

message = st.text_input("Enter a message")
if st.button("Predict"):
  prediction = model.predict(vectorizer.transform([message]))

  if prediction == 1:
    st.write("Spam")
  else:
    st.write("Not spam") 