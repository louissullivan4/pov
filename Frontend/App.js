import { StyleSheet, Text, View } from 'react-native';
import HomeScreen from './src/screens/home';

export default function App() {
  return (
    <View style={styles.container}>
      <HomeScreen/>  
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#fff',
    alignItems: 'center',
  },
});
