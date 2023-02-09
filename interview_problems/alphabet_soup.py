# def alphabet_soup(input_string: str) -> str:
#     """
#     alphabet_soup sorts a string in case-insensitive alphabetical order

#     Args:
#         input_string (str): string to sort
#     """
#     org_list: list[str] = sorted(input_string)
#     lowercase_list: list[str] = sorted(input_string.lower())

#     caps_list: list[str] = [cap for cap in org_list if cap.isupper()]

#     final_string: str = ""
#     for letter in lowercase_list:
#         if caps_list.count(letter.upper()) != 0:
#             final_string += letter.upper()
#             caps_list.pop(caps_list.index(letter.upper()))
#         else:
#             final_string += letter

#     return final_string


# print(alphabet_soup("eLEPhAnt")
print("".join(sorted(sorted("eLEPhAnt"), key=str.upper)))
