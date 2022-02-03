import * as React from 'react';
import { SafeAreaView, StyleSheet, StatusBar} from 'react-native';

import { createStackNavigator } from '@react-navigation/stack';
import { NavigationContainer } from '@react-navigation/native';

//Screens
import HomeScreen from './screens/home/index';
import ResultsScreen from './screens/results/index';

const Stack = createStackNavigator()

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <NavigationContainer>
        <Stack.Navigator screenOptions={{headerShown: false}} initialRouteName="HomeScreen">
          <Stack.Screen name="Home" component={HomeScreen} />
          <Stack.Screen name="Results" component={ResultsScreen} />
        </Stack.Navigator>
      </NavigationContainer>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex:1,
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight : 0,
    backgroundColor: "#FFF"
  },
});