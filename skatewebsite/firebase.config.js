// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyDMVQae4qMePZMME6O0GEUAGszhRYKTWA4",
    authDomain: "bloglearn-49848.firebaseapp.com",
    projectId: "bloglearn-49848",
    storageBucket: "bloglearn-49848.appspot.com",
    messagingSenderId: "600715109958",
    appId: "1:600715109958:web:639aba3132efdc86da0c47",
    measurementId: "G-ELKWVZSVGB"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);