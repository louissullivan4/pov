import { View, Text, SafeAreaView, Button } from 'react-native';
import React, { useState } from 'react';
import SearchBar from '../../components/home/seachBar';
import styles from "./styles";
import CarouselCards from '../../components/home/carouselCards';
import CategoryMenu from '../../components/home/categoryMenu';

import AppTitle from '../../components/general/appTitle';

function userSearch(navigation, searchPhrase, categoryPhrase){
  const searchTerm = searchPhrase;
  const category= categoryPhrase;
  navigation.push("Results")
}

export default function HomeScreen({ navigation }) {

  const [clicked, setClicked] = useState(false);
  const [searchPhrase, setSearchPhrase] = useState("");
  const [categoryPhrase, setCategoryPhrase] = useState("");

  return (
    <SafeAreaView style={styles.container}>
      <AppTitle/>
      <SearchBar
        searchPhrase = {searchPhrase}
        setSearchPhrase = {setSearchPhrase}
        clicked = {clicked}
        setClicked = {setClicked}
      /> 
      <View style={styles.buttonContainer}>
        <View style={styles.category}>
          <CategoryMenu
            categoryPhrase = {categoryPhrase}
            setCategoryPhrase = {setCategoryPhrase}
          />
        </View>
        <View style={styles.button}>
        <Button color="black" title="Search" onPress={() => {userSearch(navigation, searchPhrase, categoryPhrase)}}></Button>
        </View>
      </View>
      <CarouselCards/>
    </SafeAreaView>
  );
}
