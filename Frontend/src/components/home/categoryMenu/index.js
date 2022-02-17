import React, { useState }from 'react';

import DropDownPicker from 'react-native-dropdown-picker';

import styles from "./styles";

export default function CategoryMenu(props) {

  const [open, setOpen] = useState(false);
  const [value, setValue] = useState(null);
  const [items, setItems] = useState([
    {label: 'Celebrities', value: 'celebrities'},
    {label: 'Games', value: 'game'},
    {label: 'Movies ', value: 'movie'},
    {label: 'Music ', value: 'music'},
    {label: 'Politics ', value: 'politics'},
    {label: 'Product', value: 'product'},
    {label: 'Sports ', value: 'sport'},
    {label: 'Travel ', value: 'travel'}
  ]);

  return (
      <DropDownPicker
        open={open}
        value={value}
        items={items}
        setOpen={setOpen}
        setValue={setValue}
        setItems={setItems}
        onChangeValue={props.setCategoryPhrase}
        containerStyle={styles.container}
      />
  );
}