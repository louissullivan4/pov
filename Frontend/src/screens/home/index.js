import { View, Text, SafeAreaView } from 'react-native';
import React, { useState } from 'react';
import SearchBar from '../../components/home/seachBar';
import styles from "./styles";
import CarouselCards from '../../components/home/carouselCards';


export default function HomeScreen() {
  const [clicked, setClicked] = useState(false);
  const [searchPhrase, setSearchPhrase] = useState("");
  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.title}>POV</Text>
      <SearchBar
        searchPhrase = {searchPhrase}
        setSearchPhrase = {setSearchPhrase}
        clicked = {clicked}
        setClicked = {setClicked}
      /> 
      <CarouselCards/>
    </SafeAreaView>

  );
}
