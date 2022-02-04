import { View,ActivityIndicator } from 'react-native';
import React, {useState, useEffect} from 'react';
import styles from "./styles";
import ResultsWheel from '../../components/results/resultWheel';
import AppTitle from '../../components/general/appTitle';
import AppText from '../../components/general/appText';

const apiURL = "https://louissullivcs.pythonanywhere.com/imdb/rating/tt1160419";

export default function ResultsScreen() {

  const [isLoading, setLoading] = useState(true);
  const [rating, setRating] = useState(0);

  useEffect(() => {
    fetch(apiURL)
      .then((response) => response.json())
      .then((json) => {
        setRating(parseFloat(json.rating))
      
      })
      .catch((error) => alert(error))
      .finally(setLoading(false));
  })

  if (isLoading) {
    return (<ActivityIndicator/>);
  }
  else {
    return (
      <View style={styles.container}>
        <View style={{margin:10,}}>
          <AppTitle/>
        </View>
        <View style={{margin:10,}}>
          <ResultsWheel rating={rating} />
        </View>
        <View style={styles.rowContainer}>
          <View style={{justifyContent:'flex-start', padding:10}}>
            <AppText>Most popular comments:</AppText>
          </View>
        </View>
        <View style={styles.rowContainer}>
          <View style={{justifyContent:'flex-start', padding:10}}>
            <AppText>Most recent comments:</AppText>
          </View>
        </View>

        <View style={styles.rowContainer}>
          <View style={{justifyContent:'flex-start', padding:10}}>
            <AppText>Graph:</AppText>
          </View>
        </View>
      </View>
    );
  }
}
