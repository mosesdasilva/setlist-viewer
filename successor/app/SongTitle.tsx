type SongTitleProps = {
  title: string;
};

export function SongTitle({ title }: SongTitleProps) {
  return <h1>{title}</h1>;
}
