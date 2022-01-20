import { View, Text, SafeAreaView } from 'react-native';
import React, { useState } from 'react';
import SearchBar from '../../components/home/seachBar';
import styles from '../../components/home/seachBar/styles';

export default function HomeScreen() {
  const [clicked, setClicked] = useState(false);
  const [searchPhrase, setSearchPhrase] = useState("");
  return (
    <SafeAreaView style={styles.container}>
      <SearchBar
        searchPhrase = {searchPhrase}
        setSearchPhrase = {setSearchPhrase}
        clicked = {clicked}
        setClicked = {setClicked}
      /> 
    </SafeAreaView>

  );
}
