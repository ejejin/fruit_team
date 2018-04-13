

void for_soomin()
{
    TH1D *h = new TH1D("h","h",10,1,9);
    h->SetBinContent(1,9961);
    h->SetBinContent(2,13237);
    h->SetBinContent(3,15540);
    h->SetBinContent(4,15361);
    h->SetBinContent(5,18551);
    h->SetBinContent(6,22523);
    h->SetBinContent(7,19970);
    h->SetBinContent(8,15734);
    h->SetBinContent(9,14782);

    h->Draw("e");


}
