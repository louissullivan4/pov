import { View, TextInput, Button, Keyboard, SafeAreaView } from "react-native";
import React from "react";
import styles from "./styles";

import { IconButton } from 'react-native-paper';

export default function SearchBar(props) {
  return (
    <View style={styles.container}>
      <TextInput 
        style={styles.textInput}
        placeholder="Search"
        value={props.searchPhrase}
        onChangeText={props.setSearchPhrase}/>
      <IconButton
              icon="magnify"
              size={30}
              onPress={props.setFunction}
      />
    </View>

  );
}
