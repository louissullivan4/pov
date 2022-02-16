import { View, SafeAreaView, Button, Alert, Text, LogBox, Keyboard} from 'react-native';
import React, { useState, useEffect  } from 'react';
import styles from "./styles";

import SearchBar from '../../components/home/seachBar';

import CarouselCards from '../../components/home/carouselCards';
import CategoryMenu from '../../components/home/categoryMenu';

import AppTitle from '../../components/general/appTitle';
import AppText from '../../components/general/appText';

import PickerBox from 'react-native-picker-box';

import { IconButton } from 'react-native-paper';



function userSearch(navigation, searchPhrase, categoryPhrase){
  let category = categoryPhrase.toLowerCase().trim();
  let search = searchPhrase.trim();
  if ((search == "")||(category == "")){
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
      searchTerm: search, 
      searchCategory: category,
    })
  }
}

export default function HomeScreen({ navigation }) {
  
  useEffect(() => {
    LogBox.ignoreLogs(['Animated: `useNativeDriver`']);
  }, [])

  const [clicked, setClicked] = useState(false);
  const [searchPhrase, setSearchPhrase] = useState("");

  const [ref, setRef] = useState(null);
  const [categoryValue, setCategoryValue] = useState(null);
  const [items, setItems] = useState([
    {label: 'Celebrity', value: 'celebrities'},
    {label: 'Game', value: 'game'},
    {label: 'Movie ', value: 'movie'},
    {label: 'Music ', value: 'music'},
    {label: 'Politics ', value: 'politics'},
    {label: 'Product', value: 'product'},
    {label: 'Sport ', value: 'sport'},
    {label: 'Travel ', value: 'travel'}
  ]);

  return (
    <SafeAreaView style={styles.container}>
      <AppTitle/>
      <SearchBar
        searchPhrase = {searchPhrase}
        setSearchPhrase = {setSearchPhrase}
        clicked = {clicked}
        setClicked = {setClicked}
        setFunction = {() => {ref.openPicker(), Keyboard.dismiss()}}
      />
      <View style={styles.title}>
        <Text style={styles.titleText}>Trending</Text>
      </View>
      <CarouselCards/>
      <PickerBox
          ref={ setRef }
          data={ items }
          onValueChange={categoryValue => (userSearch(navigation, searchPhrase, categoryValue))}
          selectedValue={ categoryValue }
          prevTextColor={ "#37dba9" }
      />
    </SafeAreaView>
  );
}
