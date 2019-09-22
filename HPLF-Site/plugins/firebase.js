import firebase from 'firebase/app'
import 'firebase/firestore'

if (!firebase.apps.length) {
  const config = {
    apiKey: process.env.FIREBASE_API_KEY,
    authDomain: "bigred2019-ec8ab.firebaseapp.com",
    databaseURL: "https://bigred2019-ec8ab.firebaseio.com",
    projectId: "bigred2019-ec8ab",
    messagingSenderId: "787750617377",
    appId: "1:787750617377:web:e1ceb545e08e1c5a517e60"
  }
  firebase.initializeApp(config)
}

export default firebase.firestore();