import { View, TextInput, Button, Keyboard } from "react-native";
import React from "react";
import styles from "./styles";
import { Feather, Entypo } from "@expo/vector-icons";

export default function SearchBar(props) {
  
  return (
    <View style={styles.container}>
      <View style = {props.clicked ? styles.searchBar__clicked : styles.searchBar__unclicked}>
      <Feather 
        name="search"
        size={20}
        color="black"
        style={{marginLeft: 1}}
      />
      <TextInput 
        style={styles.input}
        placeholder="Search"
        value={props.searchPhrase}
        onChangeText={props.setSearchPhrase}
        onFocus={() => {
          props.setClicked(true);
        }}
        />
        {props.clicked && (
          <Entypo name="cross" size={20} color="black" style={{ padding: 1 }} onPress={() => {
              props.setSearchPhrase("") 
              props.setClicked(false)
          }}/>
        )}
      </View>
    </View>
  );
}
