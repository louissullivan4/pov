import { View, SafeAreaView, Button, Alert  } from 'react-native';
import React, { useState } from 'react';
import SearchBar from '../../components/home/seachBar';
import styles from "./styles";
import CarouselCards from '../../components/home/carouselCards';
import CategoryMenu from '../../components/home/categoryMenu';

import AppTitle from '../../components/general/appTitle';

function userSearch(navigation, searchPhrase, categoryPhrase){
  const searchTerm = searchPhrase;
  const category= categoryPhrase;
  if ((searchPhrase == "")||(categoryPhrase == "")){
    Alert.alert(
      "Search Error!",
      "Please enter a value in the search bar and select a category from the dropdown menu",
      [
        { text: "OK"}
      ]
    );
  }
  else {
    navigation.push('Results', {
      searchTerm: searchTerm, 
      searchCategory: category,
    })
  }
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
          <CategoryMenu
              categoryPhrase = {categoryPhrase}
              setCategoryPhrase = {setCategoryPhrase}
          />
          <View>
            <Button color="black" title="Search" onPress={() => {userSearch(navigation, searchPhrase, categoryPhrase)}} styles={styles.button}/> 
          </View>
      </View>
      <CarouselCards/>
    </SafeAreaView>
  );
}
