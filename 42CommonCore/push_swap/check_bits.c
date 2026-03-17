int check_bits(int num, int pos)
{
    if (pos < 0)
        return (0);
    return (num>>pos)&1;
}

void    bit_result(int top_num, int bit)
{
    if (check_bits(top_num, bit) == 0)
        pb();
    else
        ra();
}