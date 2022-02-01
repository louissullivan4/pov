import { SafeAreaView, StyleSheet, StatusBar, Text} from 'react-native';
import AppTitle from './src/components/general/appTitle';
import HomeScreen from './src/screens/home';
import ResultsScreen from './src/screens/results';



export default function App() {
  return (
      <SafeAreaView style={styles.container}>
        <ResultsScreen/>
     
      </SafeAreaView>
    );
}

const styles = StyleSheet.create({
  container: {
    flex:1,
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight : 0,
  },
});

// Colours:
// Light Green: #c8e8df
// Medium Green:#8fcdba
// Dark Green: #6e867f