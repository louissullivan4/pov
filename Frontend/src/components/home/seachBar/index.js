import { View, TextInput, Button, Keyboard, SafeAreaView } from "react-native";
import React from "react";
import styles from "./styles";


export default function SearchBar(props) {
  
  return (
    <SafeAreaView style={styles.container}>
      <TextInput 
        style={styles.textInput}
        placeholder="Search"
        value={props.searchPhrase}
        onChangeText={props.setSearchPhrase}
        />
    </SafeAreaView>
  );
}
