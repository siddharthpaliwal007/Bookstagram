import React, { useState } from 'react';

const CustomDropdown = ({ defaultLabel, options, onChangeOption, valueWithLabel, ...rest }) => {
    const [selectedOption, setSelectedOption] = useState(defaultLabel);

    return (
        <select
            value={selectedOption}

            onChange={e => {
                setSelectedOption(e.target.value)
                if (valueWithLabel) {
                    onChangeOption({ label: e.target.options[e.target.selectedIndex].text, value: e.target.value })
                }
                else {
                    onChangeOption(e.target.value)
                }
            }}
            {...rest}
        >
            <option value={defaultLabel} disabled>
                {defaultLabel}
            </option>
            {options && options.map(({ label, value }, i) => (
                <option key={i} value={value}>{label ? label : value}</option>
            ))}
        </select>
    )
}

CustomDropdown.defaultProps = {
    defaultLabel: "Choose an option",
    options: [],
    valueWithLabel: false
};

export default CustomDropdown;