from Utils import Utils

def main():
    f = open("summaries.clean.txt", "rb")
    summaries = f.readlines()
    used_words = []
    for i, summary_line in enumerate(summaries):
        summary_line = summary_line.replace('.','');
        summary_line = summary_line.replace(',','');
        summary_line = summary_line.replace('!','');
        summary_line = summary_line.replace('?','');
        summary_line = summary_line.replace('-','');
        summary_line = summary_line.strip()
        summary_words = summary_line.split(' ')
        for i, word in enumerate(summary_words):
            if word in Utils.last_names:
                if not word in used_words:
                    used_words.append(word)

    print used_words

if __name__ == '__main__':
    main()
