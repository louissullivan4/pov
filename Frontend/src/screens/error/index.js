import { View, Text, SafeAreaView, Button } from 'react-native';
import React, { useState } from 'react';
import styles from "./styles";

import AppText from '../../components/general/appText';
import AppTitle from '../../components/general/appTitle';


export default function ErrorScreen({ navigation }) {

  return (
    <SafeAreaView style={styles.container}>
      <AppTitle/>
      <View style={styles.errorContainer}>
        <AppText>Error!</AppText>
        <AppText>Looks like we messed up...</AppText>
        <View style={styles.buttons}>
        <Button color="#11edaf" title="Go to home." onPress={() => navigation.popToTop()}></Button>
        </View>
      </View>
    </SafeAreaView>
  );
}
