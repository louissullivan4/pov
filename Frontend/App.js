import { SafeAreaView, StyleSheet, Text, View } from 'react-native';
import ResultsWheel from './src/components/results/resultWheel';
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
  },
});
